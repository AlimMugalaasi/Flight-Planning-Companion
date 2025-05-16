from openai import OpenAI
from dotenv import load_dotenv
import os

# Load the .env file
load_dotenv()

# Get the key from environment
api_key = os.getenv("OPENAI_API_KEY")
client = OpenAI(api_key=api_key)

response = client.chat.completions.create(
    model="gpt-3.5-turbo",
    messages=[
        {"role": "system", "content": "You are a helpful flight planning assistant."},
        {"role": "user", "content": "Can I fly VFR from EGSX to EGMC in a C152 with weather 210/12, 9999, SCT025?"}
    ]
)

print(response.choices[0].message.content)
