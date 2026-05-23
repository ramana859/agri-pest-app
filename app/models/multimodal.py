from PIL import Image
from app.models.inference import disease_model

class MultimodalAdvisor:
    def __init__(self):
        print("✅ Multimodal Advisor initialized")

    def analyze(self, image: Image.Image, text_query: str = ""):
        # Get vision prediction
        vision_result = disease_model.predict(image)
        
        # Simple text understanding (will improve with real LLM later)
        query_lower = text_query.lower()
        
        response = {
            "vision_prediction": vision_result,
            "user_query": text_query,
            "combined_advice": vision_result["recommendation"],
            "note": "Multimodal feature activated. You can now ask questions in Hindi or English."
        }
        
        if "hindi" in query_lower or "नीम" in query_lower or "treatment" in query_lower:
            response["combined_advice"] += "\n\nहिंदी में सलाह: नीम का तेल स्प्रे करें। प्रभावित पत्तियों को हटा दें।"
        
        return response

multimodal_advisor = MultimodalAdvisor()
