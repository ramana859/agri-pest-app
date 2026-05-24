from datetime import datetime

class PriceService:
    def __init__(self):
        print("✅ Real-time Price Service Ready")

    async def get_price(self, crop: str = "tomato"):
        """Simulated real market prices (will connect to Agmarknet later)"""
        
        price_db = {
            "tomato": {
                "modal": 3450, "min": 2900, "max": 4800,
                "trend": "Rising", "unit": "₹/Quintal"
            },
            "brinjal": {
                "modal": 2800, "min": 2200, "max": 3900,
                "trend": "Stable", "unit": "₹/Quintal"
            },
            "onion": {
                "modal": 4200, "min": 3800, "max": 5500,
                "trend": "Falling", "unit": "₹/Quintal"
            }
        }
        
        crop_lower = crop.lower()
        data = price_db.get(crop_lower, price_db["tomato"])
        
        return {
            "crop": crop.capitalize(),
            "modal_price": data["modal"],
            "min_price": data["min"],
            "max_price": data["max"],
            "trend": data["trend"],
            "unit": data["unit"],
            "last_updated": datetime.now().strftime("%d %B, %Y"),
            "source": "Simulated (Agmarknet integration coming soon)",
            "advice": "Sell if price is above modal. Hold if trend is rising."
        }

price_service = PriceService()
