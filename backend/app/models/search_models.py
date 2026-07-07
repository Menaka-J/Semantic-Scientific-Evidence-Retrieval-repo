from pydantic import BaseModel
from typing import List, Optional


class SearchRequest(BaseModel):
    query: str
    top_k: int = 10


class SearchResult(BaseModel):
    doc_id: int
    title: str
    abstract: str
    score: float
    raw_score: Optional[float] = None


class SearchResponse(BaseModel):
    method: str
    total_results: int
    results: List[SearchResult]