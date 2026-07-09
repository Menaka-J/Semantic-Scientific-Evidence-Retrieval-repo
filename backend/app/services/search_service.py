from app.retrieval.tfidf_retriever import TFIDFRetriever
from app.retrieval.bm25_retriever import BM25Retriever
from app.retrieval.semantic_retriever import SemanticRetriever


class SearchService:

    def __init__(self, papers, preprocessor):

        self.tfidf = TFIDFRetriever(
            papers,
            preprocessor
        )

        self.bm25 = BM25Retriever(
            papers,
            preprocessor
        )

        self.semantic = SemanticRetriever(
            papers
        )

    def search(self, method, query, top_k):

        if method == "tfidf":

            return self.tfidf.search(
                query,
                top_k
            )

        if method == "bm25":

            return self.bm25.search(
                query,
                top_k
            )

        if method == "semantic":

            return self.semantic.search(
                query,
                top_k
            )

        raise ValueError(
            "Invalid retrieval method."
        )