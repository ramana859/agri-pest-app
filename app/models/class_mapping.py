# Expanded mapping for common diseases
CLASS_MAPPING = {
    0: "Healthy",
    1: "Early Blight (Tomato)",
    2: "Late Blight (Tomato)",
    3: "Leaf Miner",
    4: "Fruit Borer",
    5: "Bacterial Spot",
    6: "Spider Mites",
    7: "Powdery Mildew",
    8: "Tomato Mosaic Virus",
    9: "Eggplant Shoot Borer",
    10: "Target Spot",
    11: "Septoria Leaf Spot",
    12: "Other Disease"
}

def get_disease_name(class_idx: int):
    """Return disease name based on model output"""
    return CLASS_MAPPING.get(class_idx % len(CLASS_MAPPING), f"Unknown Disease (Class {class_idx})")

print("✅ Improved disease mapping loaded")
