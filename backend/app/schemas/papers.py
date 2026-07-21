from pydantic import BaseModel

class Paper(BaseModel):
    id: str
    title: str
    authors: list[str]
    published: str
    abstract: str
    pdf_url: str
    arxiv_url: str

class PaperSearchResponse(BaseModel):
    papers: list[Paper]
