import requests
from settings import settings
import numpy as np

def generateEmbedding(text):

    r = requests.get(f"{settings.embedding_url}/query", params={"text":text}, timeout=10)
    r.raise_for_status()
    
    data = r.json()

    if "embedding" not in data:
        raise ValueError(f"Unexpected response format: {data}")

    return data["embedding"]

