import torch
import torch.nn as nn
from torchvision import models
import os

print("🚀 Day 25 - First Training Step")

# Load model
model = models.efficientnet_b0(weights=None)
num_features = model.classifier[1].in_features
model.classifier = nn.Sequential(
    nn.Dropout(p=0.3),
    nn.Linear(num_features, 38)
)

# Dummy training step (we will use real data later)
optimizer = torch.optim.Adam(model.parameters(), lr=0.001)
criterion = nn.CrossEntropyLoss()

print("✅ Training components ready")
print("Performing 1 dummy training step...")

# Dummy forward pass
dummy_input = torch.randn(4, 3, 224, 224)
dummy_labels = torch.randint(0, 38, (4,))

outputs = model(dummy_input)
loss = criterion(outputs, dummy_labels)

optimizer.zero_grad()
loss.backward()
optimizer.step()

print(f"✅ Dummy training step completed. Loss: {loss.item():.4f}")

# Save model
os.makedirs("app/models", exist_ok=True)
torch.save(model.state_dict(), "app/models/plant_disease_model.pth")
print("✅ Model updated and saved!")
