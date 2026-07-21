from fastapi import APIRouter
from app.schemas.papers import PaperSearchResponse

router = APIRouter()

@router.get("/papers", response_model=PaperSearchResponse) # 이 API는 이런 형태의 JSON을 반환합니다
def get_papers():
    return {
        "papers": []
    }

