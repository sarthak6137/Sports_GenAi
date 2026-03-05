from pydantic import BaseModel

class ContentResponse(BaseModel):
    success: bool
    article: str
    context_used: bool