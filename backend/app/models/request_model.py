from pydantic import BaseModel, Field

class ContentRequest(BaseModel):
    sport: str = Field(..., description="The sport being discussed (e.g., Cricket)")
    content_type: str = Field(..., description="Type of content (e.g., Match Recap)")
    match_title: str = Field(..., description="Title of the match")
    highlights: str = Field(..., description="Key statistics and highlights")
    tone: str = Field(default="Professional", description="Writing tone")
    length: str = Field(default="Medium", description="Length of the article")