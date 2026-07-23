# GET /papers

논문를 검색합니다.

## Query

| Name | Type | Required | Description |
|------|------|----------|-------------|
| query | string | ✅ | 검색어 |
| limit | int | ❌ | 최대 결과 개수 (기본값 10) |

## Response

{
  "papers": [
    {
      "id": "...",
      "title": "...",
      "authors": [],
      "published": "...",
      "abstract": "...",
      "pdf_url": "...",
      "arxiv_url": "..."
    }
  ]
}