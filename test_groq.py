from groq import Groq
import os

# Use environment variable for API key
client = Groq(api_key=os.environ.get("GROQ_API_KEY"))

chat_completion = client.chat.completions.create(
    model="llama-3.1-8b-instant", 
    messages=[
        {"role": "system", "content": "You are a helpful assistant."},
        {"role": "user", "content": "Hello Groq! Can you confirm you’re working?"}
    ],
    temperature=0.7,
    max_tokens=200,
)

print(chat_completion.choices[0].message.content)




