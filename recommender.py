# recommender.py
import pandas as pd
import numpy as np
from utils.embedder import get_embedding

# Load assessment data and compute embeddings (just once)
data = pd.read_csv("data/shl_assessments.csv")
data_embeddings = [get_embedding(text) for text in data['description']]
data_embeddings = np.array(data_embeddings)

def recommend_assessments(query, top_n=5):
    query_embedding = get_embedding(query)
    distances = [np.linalg.norm(query_embedding - emb) for emb in data_embeddings]
    top_indices = np.argsort(distances)[:top_n]

    results = []
    for idx in top_indices:
        row = data.iloc[idx]
        results.append({
            "name": str(row['name']),
            "url": str(row['url']),
            "duration": int(row['duration']),
            "remote": str(row['remote']),
            "adaptive": str(row['adaptive']),
            "type": str(row['type'])
        })
    return results

