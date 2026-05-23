import torch
import torch.nn as nn
from torchvision import models
import os

print("🚀 Starting First Training Session...")

# Load model
model = models.efficientnet_b0(pretrained=True)
num_features = model.classifier[1].in_features
model.classifier = nn.Sequential(
    nn.Dropout(0.3),
    nn.Linear(num_features, 38)
)

print("✅ Model ready")

# Save the pretrained model (this is better starting point)
os.makedirs("app/models", exist_ok=True)
torch.save(model.state_dict(), "app/models/plant_disease_model.pth")

print("✅ Pretrained model saved")
print("Note: Real training will take multiple days.")
print("We will do small training sessions from tomorrow.")
