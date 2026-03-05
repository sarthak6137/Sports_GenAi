import os
import time
import google.generativeai as genai
from dotenv import load_dotenv
from langchain_google_genai import ChatGoogleGenerativeAI
from langchain_core.messages import HumanMessage
from app.utils.logger import logger

load_dotenv()
api_key = os.getenv("GOOGLE_API_KEY")

# 1. AUTO-DISCOVERY with Flash Prioritization
try:
    genai.configure(api_key=api_key)
    models = [m.name for m in genai.list_models() if 'generateContent' in m.supported_generation_methods]
    
    # We force Flash because 'Pro' often has a '0' limit on unverified free accounts
    flash_models = [m for m in models if "flash" in m.lower()]
    selected_model = flash_models[0] if flash_models else "models/gemini-1.5-flash"
    
    logger.info(f"AI Model Selected: {selected_model}")
except Exception as e:
    logger.error(f"Discovery failed: {e}")
    selected_model = "models/gemini-1.5-flash"

# 2. Initialize LLM
llm = ChatGoogleGenerativeAI(
    model=selected_model, 
    temperature=0.7, 
    google_api_key=api_key,
    max_retries=3 # Built-in retry logic
)

def generate_article(prompt: str, context: str) -> str:
    combined_prompt = f"Context: {context}\n\nInstruction: {prompt}"
    
    # Manually handle the 429 wait time if the built-in retry isn't enough
    for attempt in range(3):
        try:
            logger.info(f"Generating article (Attempt {attempt + 1})...")
            response = llm.invoke([HumanMessage(content=combined_prompt)])
            return response.content if hasattr(response, 'content') else str(response)
        except Exception as e:
            if "429" in str(e):
                wait_time = (attempt + 1) * 5 # Wait 5s, then 10s...
                logger.warning(f"Quota hit! Waiting {wait_time}s before retrying...")
                time.sleep(wait_time)
            else:
                logger.error(f"LLM API failure: {str(e)}")
                raise e
    
    raise Exception("AI is currently overloaded. Please try again in a minute.")