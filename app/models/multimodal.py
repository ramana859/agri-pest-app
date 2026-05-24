from PIL import Image
from app.models.inference import disease_model
from app.services.price_service import price_service

class MultimodalAdvisor:
    def __init__(self):
        print("✅ Multimodal + Price Advisor Ready")

    async def analyze(self, image: Image.Image, text_query: str = ""):
        vision_result = disease_model.predict(image)
        price_info = await price_service.get_price("tomato")   # Can make dynamic later
        
        return {
            "crop": vision_result.get("crop", "Tomato / Brinjal"),
            "disease": vision_result["disease"],
            "confidence": vision_result["confidence"],
            "market_price": price_info,
            "recommendation": vision_result["recommendation"],
            "price_advice": price_info["advice"],
            "note": "Combined AI + Market Advisory"
        }

multimodal_advisor = MultimodalAdvisor()
