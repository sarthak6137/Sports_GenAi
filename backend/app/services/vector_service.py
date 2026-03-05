import os
from dotenv import load_dotenv # This tool reads the .env file
from langchain_community.vectorstores import FAISS
from langchain_google_genai import GoogleGenerativeAIEmbeddings
from app.utils.logger import logger

# 1. Tell Python to find and read your .env file
load_dotenv()

# 2. Get the key from the file (this searches for GOOGLE_API_KEY=...)
api_key = os.getenv("GOOGLE_API_KEY")

# 3. Use the key safely
embeddings = GoogleGenerativeAIEmbeddings(
    model="models/gemini-embedding-001", 
    google_api_key=api_key
)

vector_db = None

def load_documents() -> list:
    return [
        "In cricket, a century is a score of 100 or more runs in a single innings by a batsman.",
        "A bowler taking 3 wickets in an ODI is considered a strong performance.",
        "Australia and India have a historic cricket rivalry, particularly in ODI formats.",
        "A 'Yorker' is a ball bowled to hit the pitch right at the batsman's feet."
    ]

def create_embeddings(texts: list):
    global vector_db
    try:
        vector_db = FAISS.from_texts(texts, embeddings)
        logger.info("Vector database successfully populated with embeddings.")
    except Exception as e:
        logger.error(f"Failed to create embeddings: {str(e)}")
        raise e

def initialize_vector_db():
    logger.info("Initializing Vector Database...")
    texts = load_documents()
    create_embeddings(texts)

def retrieve_similar_documents(query: str, k: int = 2) -> str:
    if not vector_db:
        logger.warning("Vector DB not initialized.")
        return ""
    
    docs = vector_db.similarity_search(query, k=k)
    context = "\n".join([doc.page_content for doc in docs])
    return context