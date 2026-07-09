import faiss

import numpy as np

from pathlib import Path

from app.services.embedding_service import EmbeddingService


class SemanticRetriever:

    def __init__(self, papers):

        self.papers = papers

        self.embedding_service = EmbeddingService()

        self.embedding_folder = Path("embeddings")

        self.embedding_folder.mkdir(exist_ok=True)

        self.embedding_file = self.embedding_folder / "embeddings.npy"

        self.index_file = self.embedding_folder / "faiss.index"

        if self.embedding_file.exists():

            print("Loading cached embeddings...")

            self.embeddings = self.embedding_service.load(

                self.embedding_file

            )

        else:

            print("Generating embeddings...")

            self.embeddings = self.embedding_service.generate(

                papers

            )

            self.embedding_service.save(

                self.embeddings,

                self.embedding_file

            )

        dimension = self.embeddings.shape[1]

        if self.index_file.exists():

            self.index = faiss.read_index(

                str(self.index_file)

            )

        else:

            self.index = faiss.IndexFlatIP(

                dimension

            )

            self.index.add(

                self.embeddings.astype(

                    np.float32

                )

            )

            faiss.write_index(

                self.index,

                str(self.index_file)

            )

    def search(self, query, top_k=10):

        vector = self.embedding_service.encode_query(

            query

        )

        scores, indices = self.index.search(

            np.array(

                [vector],

                dtype=np.float32

            ),

            top_k

        )

        results = []

        for score, idx in zip(

            scores[0],

            indices[0]

        ):

            paper = self.papers[idx]

            results.append({

                "doc_id": paper["doc_id"],

                "title": paper["title"],

                "abstract": paper["abstract"],

                "score": float(score)

            })

        return results