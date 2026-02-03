from pydantic import BaseModel, RootModel

class QueryRequest(BaseModel):
    query: str
    n_rewrites: int
    n_chunks: int

class QueryCorpusRequest(BaseModel):
    query: str
    n_rewrites: int
    n_chunks: int
    corpus: str | None

class QueryResponse(BaseModel):
    chunks: list
    metadata: list

class ABItem(BaseModel):
    corpus: str
    data: QueryResponse

class ABTestResponse(RootModel[list[ABItem]]):
    pass
