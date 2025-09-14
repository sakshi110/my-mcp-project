 My MCP Project

This project is an MCP server that fetches weather data (from OpenWeather & wttr.in as fallback) 
and integrates with Groq LLM to summarize it.

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

