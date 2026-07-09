from pathlib import Path
import joblib
import numpy as np


def save_embeddings(path, embeddings):
    np.save(path, embeddings)


def load_embeddings(path):
    return np.load(path)


def save_metadata(path, metadata):
    joblib.dump(metadata, path)


def load_metadata(path):
    return joblib.load(path)