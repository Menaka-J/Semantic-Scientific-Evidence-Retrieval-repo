from app.retrieval.tfidf_retriever import TFIDFRetriever
from app.retrieval.bm25_retriever import BM25Retriever


class SearchService:

    def __init__(self, papers, preprocessor):
        self.tfidf = TFIDFRetriever(papers, preprocessor)
        self.bm25 = BM25Retriever(papers, preprocessor)

    def search(self, method: str, query: str, top_k: int):

        if method == "tfidf":
            return self.tfidf.search(query, top_k)

        elif method == "bm25":
            return self.bm25.search(query, top_k)

        raise ValueError("Invalid retrieval method.")