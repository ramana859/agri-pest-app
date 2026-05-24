from fastapi import APIRouter, UploadFile, File, Form
from PIL import Image
import io
from app.models.multimodal import multimodal_advisor

router = APIRouter(prefix="/disease", tags=["Disease Detection"])

@router.post("/detect")
async def detect_disease(
    image: UploadFile = File(...),
    query: str = Form("")  
):
    try:
        contents = await image.read()
        pil_image = Image.open(io.BytesIO(contents))
        
        result = await multimodal_advisor.analyze(pil_image, query)
        
        return {
            "status": "success",
            "filename": image.filename,
            "analysis": result
        }
    except Exception as e:
        return {
            "status": "error",
            "message": "Failed to process image",
            "detail": str(e)
        }
