from deep_translator import GoogleTranslator
from langdetect import detect, DetectorFactory
import logging

# For consistent language detection
DetectorFactory.seed = 0

def detect_language(text: str) -> str:
    if not text or len(text.strip()) < 2:
        return "en"
    try:
        return detect(text)
    except:
        return "en"

def translate_to_english(text: str) -> str:
    """Translate Hindi/Hinglish to English"""
    if not text:
        return ""
    
    try:
        lang = detect_language(text)
        if lang == "en":
            return text
        
        translator = GoogleTranslator(source="auto", target="en")
        return translator.translate(text)
    except Exception as e:
        print(f"Translation error: {e}")
        return text  # fallback


def translate_to_hindi(text: str) -> str:
    """Translate English to Hindi"""
    try:
        translator = GoogleTranslator(source="auto", target="hi")
        return translator.translate(text)
    except Exception as e:
        print(f"Hindi translation error: {e}")
        return text
