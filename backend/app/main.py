from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from app.api.papers import router as papers_router

import arxiv

app = FastAPI()

@app.get("/")
def root():
    return {"message": "Hello MyArxiv!"}

app.include_router(papers_router)