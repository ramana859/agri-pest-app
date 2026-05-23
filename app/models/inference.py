from PIL import Image
import torch
from torchvision import models, transforms
import torch.nn as nn
from app.models.class_mapping import get_disease_name
from app.models.crop_detector import crop_detector

class DiseaseInference:
    def __init__(self):
        self.transform = transforms.Compose([
            transforms.Resize((224, 224)),
            transforms.ToTensor(),
            transforms.Normalize(mean=[0.485, 0.456, 0.406], 
                               std=[0.229, 0.224, 0.225])
        ])
        
        self.model = models.efficientnet_b0(pretrained=False)
        num_features = self.model.classifier[1].in_features
        self.model.classifier = nn.Sequential(
            nn.Dropout(p=0.2),
            nn.Linear(num_features, 38)
        )
        
        try:
            self.model.load_state_dict(torch.load("app/models/plant_disease_model.pth", weights_only=True))
            print("✅ Disease model loaded")
        except:
            print("⚠️ Using untrained model")
        
        self.model.eval()

    def predict(self, image: Image.Image):
        img_tensor = self.transform(image).unsqueeze(0)
        
        with torch.no_grad():
            outputs = self.model(img_tensor)
            probabilities = torch.softmax(outputs, dim=1)[0]
            confidence, predicted_idx = torch.max(probabilities, 0)
        
        disease_name = get_disease_name(predicted_idx.item())
        crop_info = crop_detector.detect_crop(image)
        
        return {
            "disease": disease_name,
            "confidence": round(confidence.item() * 100, 2),
            "crop": crop_info["crop"],
            "recommendation": "• Remove infected leaves immediately\n• Spray Neem oil (5ml per liter water)\n• Avoid overhead watering",
            "note": "Model is under training. Low confidence expected."
        }

disease_model = DiseaseInference()
