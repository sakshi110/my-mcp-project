


import os
import httpx
from fastapi import FastAPI

app = FastAPI()

OPENWEATHER_KEY = os.getenv("OPENWEATHER_API_KEY")

@app.get("/weather/{city}")
async def get_weather(city: str):
    try:
        if OPENWEATHER_KEY:
            url = f"http://api.openweathermap.org/data/2.5/weather?q={city}&appid={OPENWEATHER_KEY}&units=metric"
            async with httpx.AsyncClient(timeout=10) as client:
                resp = await client.get(url)
                if resp.status_code == 200:
                    data = resp.json()
                    return {
                        "source": "OpenWeather",
                        "city": data["name"],
                        "temperature": data["main"]["temp"],
                        "condition": data["weather"][0]["description"]
                    }
                else:
                    # fallback to wttr.in
                    raise Exception("OpenWeather failed")
        
        # fallback to wttr.in
        async with httpx.AsyncClient(timeout=10) as client:
            resp = await client.get(f"http://wttr.in/{city}?format=j1")
            resp.raise_for_status()
            data = resp.json()
            current = data["current_condition"][0]
            return {
                "source": "wttr.in",
                "city": city,
                "temperature": current["temp_C"],
                "condition": current["weatherDesc"][0]["value"]
            }
    except Exception as e:
        return {"error": str(e), "hint": "Check API key or internet"}
