from app.models.request_model import ContentRequest

def build_prompt(data: ContentRequest) -> str:
    template = """You are a professional sports journalist writing for a global sports media platform.
Write a detailed {content_type} for the following sports event.

Sport: {sport}
Match: {match_title}
Highlights: {highlights}
Tone: {tone}
Length: {length}

Use the following structure:
- Title
- Match Overview
- Key Moments
- Player Performances
- Turning Points
- Conclusion

Ensure the tone is professional and uses correct sports terminology."""

    return template.format(
        content_type=data.content_type,
        sport=data.sport,
        match_title=data.match_title,
        highlights=data.highlights,
        tone=data.tone,
        length=data.length
    )