from fastapi import FastAPI
from models.models import QueryRequest, QueryResponse
from query.query import rewrite_and_query
from data.database import get_chroma_collection

app = FastAPI()

collection = get_chroma_collection()

@app.post("/query", response_model=QueryResponse)
def handle_query(payload: QueryRequest):

    docs, metas = rewrite_and_query(payload.query, collection = collection, n_rewrites = payload.n_rewrites, n_chunks = payload.n_chunks)

    return {"chunks": docs, "metadata": metas}