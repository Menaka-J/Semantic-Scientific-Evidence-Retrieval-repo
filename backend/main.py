from pathlib import Path

from fastapi import FastAPI

from fastapi.middleware.cors import CORSMiddleware

from app.data.dataset_loader import DatasetLoader

from app.preprocessing.text_preprocessor import TextPreprocessor

from app.retrieval.tfidf_retriever import TFIDFRetriever

from app.retrieval.bm25_retriever import BM25Retriever

BASE_DIR = Path(__file__).resolve().parent.parent

DATASET = BASE_DIR / "dataset" / "SciFact" / "corpus.jsonl"

loader = DatasetLoader(DATASET)

papers = loader.load_corpus()

processor = TextPreprocessor()

tfidf = TFIDFRetriever(

    papers,

    processor

)

bm25 = BM25Retriever(

    papers,

    processor

)

app = FastAPI(

    title="Semantic Scientific Evidence Retrieval"

)

app.add_middleware(

    CORSMiddleware,

    allow_origins=["*"],

    allow_credentials=True,

    allow_methods=["*"],

    allow_headers=["*"]

)

@app.get("/")

def home():

    return {

        "documents": len(papers),

        "methods": [

            "tfidf",

            "bm25"

        ]

    }

@app.get("/health")

def health():

    return {

        "status": "running"

    }

@app.get("/search/tfidf")

def tfidf_search(

    query: str,

    top_k: int = 10

):

    return tfidf.search(

        query,

        top_k

    )

@app.get("/search/bm25")

def bm25_search(

    query: str,

    top_k: int = 10

):

    return bm25.search(

        query,

        top_k

    )