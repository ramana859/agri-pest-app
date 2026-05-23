import torch
import torch.nn as nn
from torchvision import models

def create_model(num_classes=38):
    """Create base model"""
    model = models.efficientnet_b0(pretrained=True)
    
    # Modify classifier for our disease classes
    num_features = model.classifier[1].in_features
    model.classifier = nn.Sequential(
        nn.Dropout(p=0.2),
        nn.Linear(num_features, num_classes)
    )
    
    print(f"✅ Model created with {num_classes} output classes")
    print("This model will be fine-tuned for Tomato & Brinjal diseases later")
    return model

if __name__ == "__main__":
    model = create_model()
    # Save the model
    import os
    os.makedirs("app/models", exist_ok=True)
    torch.save(model.state_dict(), "app/models/plant_disease_model.pth")
    print("✅ Initial model weights saved successfully!")
