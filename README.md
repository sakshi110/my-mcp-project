 My MCP Project

This project is an MCP (Model Context Protocol) server that fetches live weather data from OpenWeather (with wttr.in as a fallback) and integrates with Groq LLM to generate natural language summaries of the weather.

✨ Features

Fetches current weather for any city 🌍

Uses OpenWeather API (with API key)

Falls back to wttr.in if OpenWeather fails

Integrates with Groq’s LLM for smart weather summaries 🤖

Built with FastAPI for easy local server hosting

## Run locally
1. Clone the repo:
   git clone https://github.com/sakshi110/my-mcp-project.git
2. Install dependencies:
   pip install -r requirements.txt
3. Set your API key:
   $env:OPENWEATHER_API_KEY='your_api_key'
4. Run the server:
   py -m uvicorn mini_weather:app --reload
5. Test in browser:
   http://127.0.0.1:8000/weather/London




##Example Usage

##Check weather for London:

http://127.0.0.1:8000/weather/London


##Run Groq integration:

py groq_weather.py London




my-mcp-project/
│── mini_weather.py    # FastAPI MCP server
│── weather_mcp.py     # Weather data fetcher
│── groq_weather.py    # Groq integration for summaries
│── test_groq.py       # Test script
│── requirements.txt   # Dependencies
│── README.md          # Project documentation









