from fastapi import FastAPI
from models.models import QueryRequest, QueryResponse, ABTestResponse, ABItem
from query.query import rewrite_and_query
from data.database import get_chroma_collection
import random
from settings import settings

app = FastAPI()

collection_docs = get_chroma_collection(settings.collection_name)
collection_manual = get_chroma_collection("Tools")
collection_combined = get_chroma_collection("Combined")

AB_OPTIONS = {
    "Documents": collection_docs,
    "Tools": collection_manual,
    "Combined": collection_combined,
    "None": None,
}

def run_ABquery(query, collection, n_rewrites, n_chunks):

    if collection is None:
        return QueryResponse(chunks=[], metadata=[])

    docs, metas = rewrite_and_query(
        query,
        collection=collection,
        n_rewrites=n_rewrites,
        n_chunks=n_chunks,
    )

    return QueryResponse(chunks=docs, metadata=metas)

@app.post("/query", response_model=QueryResponse)
def handle_query(payload: QueryRequest):

    docs, metas = rewrite_and_query(payload.query, collection = collection_docs, n_rewrites = payload.n_rewrites, n_chunks = payload.n_chunks)

    return QueryResponse(chunks=docs, metadata=metas)

@app.post("/queryab", response_model=ABTestResponse)
def handle_ab_test(payload: QueryRequest):

    chosen = random.sample(list(AB_OPTIONS.keys()), k=2)

    out = []

    for name in chosen:
        collection = AB_OPTIONS[name]
        data = run_ABquery(
            query=payload.query,
            collection=collection,
            n_rewrites=payload.n_rewrites,
            n_chunks=payload.n_chunks,
        )
        out.append(ABItem(corpus=name, data=data))

    return ABTestResponse(out)