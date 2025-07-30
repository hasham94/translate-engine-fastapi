from pydantic import BaseModel

class VideoInput(BaseModel):
    url: str
    target_language: str

class SummaryInput(BaseModel):
    text: str