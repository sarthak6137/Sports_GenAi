from fastapi import APIRouter, HTTPException
from pydantic import BaseModel
from app.services.vector_service import retrieve_similar_documents
from app.services.llm_service import generate_article
from app.utils.logger import logger

router = APIRouter()

# This MUST match the keys in your React 'formData' state
class ContentRequest(BaseModel):
    sport: str
    content_type: str
    match_title: str
    highlights: str
    tone: str
    length: str

@router.post("/generate-content")
async def create_sports_content(request: ContentRequest):
    logger.info(f"Processing {request.sport} article for {request.match_title}")
    
    try:
        # 1. Search Vector DB for sports context
        context = retrieve_similar_documents(f"{request.sport} {request.match_title}")
        
        # 2. Build the instruction for the AI
        prompt = (f"Write a {request.length} {request.content_type} about {request.match_title}. "
                  f"Tone: {request.tone}. Highlights: {request.highlights}")
        
        # 3. Call Gemini
        article_text = generate_article(prompt, context)
        
        # 4. Return the exact JSON the frontend expects
        return {
            "success": True,
            "article": article_text
        }
        
    except Exception as e:
        logger.error(f"Backend Crash: {str(e)}")
        raise HTTPException(status_code=500, detail=str(e))