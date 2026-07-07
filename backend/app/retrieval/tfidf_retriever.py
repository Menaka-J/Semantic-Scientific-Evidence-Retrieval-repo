from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.metrics.pairwise import cosine_similarity


class TFIDFRetriever:

    def __init__(self, papers, preprocessor):

        self.papers = papers
        self.preprocessor = preprocessor

        self.documents = [
            self.preprocessor.preprocess(
                paper["combined_text"]
            )
            for paper in papers
        ]

        self.vectorizer = TfidfVectorizer()

        self.matrix = self.vectorizer.fit_transform(
            self.documents
        )

    def search(self, query, top_k=10):

        query = self.preprocessor.preprocess(query)

        query_vector = self.vectorizer.transform([query])

        similarity = cosine_similarity(
            query_vector,
            self.matrix
        ).flatten()

        ranked = similarity.argsort()[::-1]

        results = []

        for idx in ranked[:top_k]:

            results.append({

                "doc_id": self.papers[idx]["doc_id"],

                "title": self.papers[idx]["title"],

                "abstract": self.papers[idx]["abstract"],

                "score": float(similarity[idx])

            })

        return results