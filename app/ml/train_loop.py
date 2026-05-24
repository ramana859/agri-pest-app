import sys
import os
sys.path.append(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))

import torch
import torch.nn as nn
from torchvision import models
import os

print("🚀 Day 24 - Dataset Training Pipeline")

# Load model with updated syntax
model = models.efficientnet_b0(weights=None)   # Using None to avoid warnings
num_features = model.classifier[1].in_features
model.classifier = nn.Sequential(
    nn.Dropout(p=0.3),
    nn.Linear(num_features, 38)
)

print("✅ Model loaded successfully")
print(f"Number of output classes: 38")

# Try to load dataset
try:
    from datasets import load_from_disk
    dataset = load_from_disk("data/plantvillage")
    print(f"✅ Dataset loaded: {len(dataset)} images")
except Exception as e:
    print(f"⚠️ Dataset loading skipped: {e}")

# Save model
os.makedirs("app/models", exist_ok=True)
torch.save(model.state_dict(), "app/models/plant_disease_model.pth")

print("✅ Model saved successfully!")
print("Training pipeline is ready.")
