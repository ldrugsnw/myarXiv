import arxiv

def search_papers(query: str):

    client = arxiv.Client(
        page_size=5,
        delay_seconds=3,
        num_retries=3
    ) # arxiv 서버와 대화하는 담당자 arxiv 서버 입장에서 고객

    search = arxiv.Search(
        query = query,
        max_results = 1,  # 최대 개수 
        sort_by = arxiv.SortCriterion.SubmittedDate,
    )

    results = client.results(search)

    papers = []

    for paper in results:

        papers.append({
            "id": paper.entry_id.split("/abs/")[1].split("v")[0],
            "title": paper.title,
            "authors" : [author.name for author in paper.authors],
            "published" : paper.published,
            "updated" : paper.updated,
            "summary" : paper.summary,
            "pdf_url" : paper.pdf_url,
        })

    return papers