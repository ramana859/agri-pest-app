from datasets import load_dataset
import os

def download_plantvillage():
    print("Downloading PlantVillage dataset (this may take time)...")
    
    # Updated loading method
    dataset = load_dataset("mohanty/PlantVillage", "default", split="train")
    
    # Save locally
    os.makedirs("data/plantvillage", exist_ok=True)
    dataset.save_to_disk("data/plantvillage")
    
    print("✅ Dataset downloaded successfully!")
    print(f"Total images: {len(dataset)}")
    print("Focus crops: Tomato, Brinjal (Eggplant), etc.")

if __name__ == "__main__":
    download_plantvillage()
