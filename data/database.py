import chromadb
from chromadb.config import Settings
from llm.llmAdapter import generateEmbedding
from settings import settings as app_settings

def get_chroma_collection(collection_name):
    client = chromadb.PersistentClient(
        path=app_settings.chroma_dir,
        settings=Settings(anonymized_telemetry=False),
    )
    try:
        collection = client.get_collection(collection_name)
    except Exception:
        raise Exception(f"Collection of name {collection_name} does not exist under dir {app_settings.chroma_dir}.")
    return collection

def query_index(query, collection, k = 5):
    query_emb = generateEmbedding(query)
    results = collection.query(
        query_embeddings=[query_emb],
        n_results=k,
    )
    return results