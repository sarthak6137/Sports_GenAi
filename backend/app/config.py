import os
from dotenv import load_dotenv

load_dotenv()

class Config:
    GOOGLE_API_KEY = os.getenv("GOOGLE_API_KEY")
    # OPENAI_API_KEY = os.getenv("OPENAI_API_KEY") # Uncomment if using OpenAI
    PORT = int(os.getenv("PORT", 8000))

config = Config()