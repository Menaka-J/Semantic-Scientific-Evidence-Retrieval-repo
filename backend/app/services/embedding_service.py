from pathlib import Path

from sentence_transformers import SentenceTransformer

from tqdm import tqdm

import numpy as np

from app.utils.file_utils import (
    save_embeddings,
    load_embeddings
)


class EmbeddingService:

    def __init__(self):

        self.model = SentenceTransformer(
            "all-MiniLM-L6-v2"
        )

    def generate(self, papers):

        embeddings = []

        for paper in tqdm(papers):

            embedding = self.model.encode(

                paper["combined_text"],

                normalize_embeddings=True

            )

            embeddings.append(embedding)

        return np.array(embeddings)

    def encode_query(self, query):

        return self.model.encode(

            query,

            normalize_embeddings=True

        )

    def save(self, embeddings, path):

        save_embeddings(path, embeddings)

    def load(self, path):

        return load_embeddings(path)