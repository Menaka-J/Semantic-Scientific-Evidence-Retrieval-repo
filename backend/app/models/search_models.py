from pydantic import BaseModel


class SearchResult(BaseModel):

    doc_id: int

    title: str

    abstract: str

    score: float