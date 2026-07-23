from pydantic import BaseModel
from datetime import datetime

class Paper(BaseModel):
    id: str
    title: str
    authors: list[str]
    published: datetime
    updated: datetime
    summary: str
    pdf_url: str

class PaperSearchResponse(BaseModel):
    papers: list[Paper]
