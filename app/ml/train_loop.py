import torch
import torch.nn as nn
from torchvision import models
import os

print("🚀 Starting Small Training Loop...")

# Load model
model = models.efficientnet_b0(pretrained=True)
num_features = model.classifier[1].in_features
model.classifier = nn.Sequential(
    nn.Dropout(0.3),
    nn.Linear(num_features, 38)
)

# Loss and optimizer
criterion = nn.CrossEntropyLoss()
optimizer = torch.optim.Adam(model.parameters(), lr=0.001)

print("✅ Training components ready")
print("Note: We will train on a small batch first to avoid long time.")

# Save current model
os.makedirs("app/models", exist_ok=True)
torch.save(model.state_dict(), "app/models/plant_disease_model.pth")

print("✅ Model saved after setup")
print("\nReal training with dataset will start from next days.")
