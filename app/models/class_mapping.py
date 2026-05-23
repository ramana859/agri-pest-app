CLASS_MAPPING = {
    0: "Healthy",
    1: "Early Blight (Tomato)",
    2: "Late Blight (Tomato)",
    3: "Leaf Miner",
    4: "Fruit Borer",
    5: "Bacterial Spot",
    6: "Spider Mites",
    7: "Target Spot",
    8: "Tomato Mosaic Virus",
    9: "Powdery Mildew",
    10: "Eggplant Fruit & Shoot Borer",
    11: "Other Disease"
}

def get_disease_name(class_idx: int):
    return CLASS_MAPPING.get(class_idx % 12, f"Unknown Disease (Class {class_idx})")

print("✅ Disease class mapping loaded")
