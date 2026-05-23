from PIL import Image
import torch
from torchvision import transforms
from app.core.config import settings

class DiseaseInference:
    def __init__(self):
        self.model = None
        self.transform = transforms.Compose([
            transforms.Resize((224, 224)),
            transforms.ToTensor(),
        ])
        print("✅ Disease Model class initialized (placeholder)")

    def predict(self, image: Image.Image):
        """Placeholder prediction - will connect real model soon"""
        # For now return dummy result
        return {
            "disease": "Early Blight (Tomato)",
            "confidence": 0.87,
            "recommendation": "Use Neem oil + remove affected leaves. Check market price before harvesting.",
            "crop": "Tomato"
        }

# Initialize model instance
disease_model = DiseaseInference()
