from dotenv import load_dotenv
load_dotenv()

from fastapi import FastAPI
# 1. NEW IMPORT: This is the security guard we need to configure
from fastapi.middleware.cors import CORSMiddleware 

from app.routes import generate_content
from app.services.vector_service import initialize_vector_db
from app.utils.logger import logger
from contextlib import asynccontextmanager

@asynccontextmanager
async def lifespan(app: FastAPI):
    try:
        initialize_vector_db()
        logger.info("Application startup complete.")
    except Exception as e:
        logger.error(f"Failed during startup: {str(e)}")
    yield
    logger.info("Application shutdown.")

app = FastAPI(title="SportsGenAI Studio API", lifespan=lifespan)

# --- 2. ADD THIS NEW BLOCK HERE ---
# This allows your React app (on port 5173) to talk to this API (on port 8000)
app.add_middleware(
    CORSMiddleware,
    allow_origins=["http://localhost:5173"], # Your React URL
    allow_credentials=True,
    allow_methods=["*"], # Allows POST, GET, etc.
    allow_headers=["*"], # Allows all headers
)
# -----------------------------------

app.include_router(generate_content.router)

@app.get("/health")
def health_check():
    return {"status": "running"}