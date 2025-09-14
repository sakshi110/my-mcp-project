import os
import httpx
from groq import Groq

# Load API keys from environment
GROQ_KEY = os.getenv("GROQ_API_KEY")
OPENWEATHER_KEY = os.getenv("OPENWEATHER_API_KEY")

# Initialize Groq client
groq_client = Groq(api_key=GROQ_KEY)

async def fetch_weather(city: str):
    """
    Try OpenWeather first, then fallback to wttr.in
    """
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
                        "temp": data["main"]["temp"],
                        "condition": data["weather"][0]["description"]
                    }
    except Exception as e:
        print("⚠️ OpenWeather failed, falling back:", e)

    # fallback
    async with httpx.AsyncClient(timeout=10) as client:
        resp = await client.get(f"http://wttr.in/{city}?format=j1")
        resp.raise_for_status()
        data = resp.json()
        current = data["current_condition"][0]
        return {
            "source": "wttr.in",
            "city": city,
            "temp": current["temp_C"],
            "condition": current["weatherDesc"][0]["value"]
        }

def summarize_weather(weather: dict):
    """
    Use Groq LLM to summarize the weather nicely
    """
    prompt = f"""
    Summarize this weather data in a friendly, human-readable way:

    City: {weather['city']}
    Temperature: {weather['temp']} °C
    Condition: {weather['condition']}
    Source: {weather['source']}
    """

    response = groq_client.chat.completions.create(
    model="llama-3.1-8b-instant",
    messages=[{"role": "user", "content": prompt}],
)


    return response.choices[0].message.content

# -------------------------
# Run directly from terminal
# -------------------------
if __name__ == "__main__":
    import asyncio, sys

    if len(sys.argv) < 2:
        print("Usage: py groq_weather.py <city>")
        sys.exit(1)

    city = sys.argv[1]
    weather = asyncio.run(fetch_weather(city))
    print("✅ Raw Weather Data:", weather)
    print("🤖 Groq Summary:\n", summarize_weather(weather))
