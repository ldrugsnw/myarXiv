from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware

import arxiv

app = FastAPI()

app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"], # 나중에 보안을 위해서 origin은 하나만 넣어야됨
    allow_credentials=False,
    allow_methods=["*"],
    allow_headers=["*"],
)

@app.get("/")
def root():
    return {"message": "Hello MyArxiv!"}

@app.get("/papers")
def get_papers():
  """  client = arxiv.Client()

    search = arxiv.Search(
        query = "LLM",
        max_results=10,
        sort_by=arxiv.SortCriterion.SubmittedDate
    )

    papers = []

    for paper in client.results(search):
        papers.append({
            "title": paper.title,
            "author": ', '.join([author.name for author in paper.authors]),
            "published_date": paper.published.date()
        })

    return papers """

  return [
        {
            "title": "test",
            "author": "shin",
            "published_date": "2026-07-17"
        }
    ]