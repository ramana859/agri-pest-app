from datasets import load_from_disk
from torchvision import transforms
from torch.utils.data import Dataset
from PIL import Image
import torch

class PlantVillageDataset(Dataset):
    def __init__(self, split="train"):
        print(f"Loading PlantVillage dataset for {split}...")
        self.dataset = load_from_disk("data/plantvillage")
        self.transform = transforms.Compose([
            transforms.Resize((224, 224)),
            transforms.ToTensor(),
            transforms.Normalize(mean=[0.485, 0.456, 0.406], 
                               std=[0.229, 0.224, 0.225])
        ])
        print(f"✅ Dataset loaded with {len(self.dataset)} images")

    def __len__(self):
        return len(self.dataset)

    def __getitem__(self, idx):
        item = self.dataset[idx]
        image = item['image']
        label = item.get('label', 0)
        
        if self.transform:
            image = self.transform(image)
        
        return image, label

print("✅ PlantVillage Dataset Loader Ready")
