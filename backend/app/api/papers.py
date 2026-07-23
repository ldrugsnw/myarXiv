from fastapi import APIRouter
from app.schemas.papers import PaperSearchResponse
from app.services.arxiv_service import search_papers

router = APIRouter()

@router.get("/papers", response_model=PaperSearchResponse) # 이 API는 이런 형태의 JSON을 반환합니다
def get_papers():

    papers = search_papers()

    return {
        "papers": papers
    }

