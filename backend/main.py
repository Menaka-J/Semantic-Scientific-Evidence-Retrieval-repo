from fastapi import FastAPI

from app.data.dataset_loader import DatasetLoader

from app.preprocessing.text_preprocessor import TextPreprocessor

from app.utils.logger import logger

app=FastAPI(title="Semantic Scientific Evidence Retrieval")

loader=DatasetLoader("../dataset/SciFact/corpus.jsonl")

papers=loader.load_corpus()

processor=TextPreprocessor()

logger.info(f"Loaded {len(papers)} papers.")

@app.get("/")

def home():

    return {

        "project":"Semantic Scientific Evidence Retrieval",

        "documents":len(papers)

    }

@app.get("/health")

def health():

    return {

        "status":"Running"

    }