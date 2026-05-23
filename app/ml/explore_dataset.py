from datasets import load_from_disk
import os

def explore_dataset():
    print("Loading saved dataset...")
    dataset = load_from_disk("data/plantvillage")
    
    print(f"✅ Dataset loaded!")
    print(f"Total images: {len(dataset)}")
    print(f"Available columns: {dataset.column_names}")
    
    # Use correct column names based on actual structure
    label_column = 'label' if 'label' in dataset.column_names else 'text'
    
    # Show class distribution
    unique_labels = set(dataset[label_column])
    print(f"Number of disease classes: {len(unique_labels)}")
    
    # Show first few examples
    print("\nSample data:")
    for i in range(min(5, len(dataset))):
        label = dataset[i][label_column]
        print(f"Image {i+1}: Label = {label}")
    
    # Save info
    os.makedirs("app/models", exist_ok=True)
    with open("app/models/class_names.txt", "w") as f:
        f.write(f"Total classes: {len(unique_labels)}\n")
        f.write(f"Label column: {label_column}\n")
        f.write("Ready for model training\n")

    print("\n✅ Dataset exploration completed successfully!")

if __name__ == "__main__":
    explore_dataset()
