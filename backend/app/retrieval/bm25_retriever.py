from rank_bm25 import BM25Okapi


class BM25Retriever:

    def __init__(self, papers, preprocessor):

        self.papers = papers

        self.preprocessor = preprocessor

        self.documents = [

            self.preprocessor.preprocess(

                paper["combined_text"]

            ).split()

            for paper in papers

        ]

        self.bm25 = BM25Okapi(self.documents)

    def search(self, query, top_k=10):

        tokens = self.preprocessor.preprocess(

            query

        ).split()

        scores = self.bm25.get_scores(tokens)

        ranked = scores.argsort()[::-1]

        results = []

        for idx in ranked[:top_k]:

            results.append({

                "doc_id": self.papers[idx]["doc_id"],

                "title": self.papers[idx]["title"],

                "abstract": self.papers[idx]["abstract"],

                "score": float(scores[idx])

            })

        return results