from pathlib import Path

from fastapi import FastAPI, HTTPException
from fastapi.middleware.cors import CORSMiddleware

from app.data.dataset_loader import DatasetLoader
from app.preprocessing.text_preprocessor import TextPreprocessor
from app.services.search_service import SearchService
from app.services.statistics import DatasetStatistics

BASE_DIR = Path(__file__).resolve().parent.parent
DATASET = BASE_DIR / "dataset" / "SciFact" / "corpus.jsonl"

loader = DatasetLoader(DATASET)
papers = loader.load_corpus()

processor = TextPreprocessor()

search_service = SearchService(
    papers,
    processor
)

statistics = DatasetStatistics(
    papers
)

app = FastAPI(
    title="Semantic Scientific Evidence Retrieval",
    version="1.0.0"
)

app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)


@app.get("/")
def root():
    return {
        "project": "Semantic Scientific Evidence Retrieval",
        "documents": len(papers),
        "methods": [
            "tfidf",
            "bm25",
            "semantic"
        ]
    }


@app.get("/health")
def health():
    return {
        "status": "running"
    }


@app.get("/statistics")
def get_statistics():
    return statistics.summary()


@app.get("/search/{method}")
def search(
    method: str,
    query: str,
    top_k: int = 10
):

    try:

        results = search_service.search(
            method,
            query,
            top_k
        )

        return {
            "method": method,
            "total_results": len(results),
            "results": results
        }

    except ValueError as e:
        raise HTTPException(
            status_code=400,
            detail=str(e)
        )