
import os
import requests
from fastapi import FastAPI
import uvicorn
from groq import Groq

# -------------------------
# Setup Groq client
# -------------------------
groq_client = Groq(api_key=os.environ.get("GROQ_API_KEY"))

# -------------------------
# Setup FastAPI
# -------------------------
app = FastAPI(title="Weather MCP API")

# -------------------------
# 
@app.get("/get_weather")
async def get_weather(city: str):
    """
    Returns live weather for a given city using OpenWeatherMap API.
    """
    api_key = os.environ.get("OPENWEATHER_API_KEY")
    if not api_key:
        return {"error": "OPENWEATHER_API_KEY not set"}

    url = f"http://api.openweathermap.org/data/2.5/weather?q={city}&appid={api_key}&units=metric"
    response = requests.get(url)

    if response.status_code != 200:
        return {"error": f"Failed to fetch weather: {response.text}"}

    data = response.json()
    description = data["weather"][0]["description"]
    temperature = data["main"]["temp"]

    return {"result": f"The weather in {city} is {description} with {temperature}°C."}
