from fastapi import APIRouter, UploadFile, File
from PIL import Image
import io
from app.models.inference import disease_model

router = APIRouter(prefix="/disease", tags=["Disease Detection"])

@router.post("/detect")
async def detect_disease(image: UploadFile = File(...)):
    """Detect disease from uploaded crop image"""
    contents = await image.read()
    pil_image = Image.open(io.BytesIO(contents))
    
    # Get prediction from model
    result = disease_model.predict(pil_image)
    
    return {
        "status": "success",
        "filename": image.filename,
        "prediction": result,
        "message": "This is a working prototype. Real AI model coming soon."
    }
