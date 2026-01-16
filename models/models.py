from pydantic import BaseModel

class QueryRequest(BaseModel):
    query: str
    n_rewrites: int
    n_chunks: int

class QueryResponse(BaseModel):
    chunks: list
    metadata: list