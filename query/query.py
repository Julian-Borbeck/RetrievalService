from data.database import query_index
from llm.rewritingAdapter import rewrite_query_k_times

def rewrite_and_query(user_query, collection, n_rewrites = 5, n_chunks = 20):
    queries = rewrite_query_k_times(user_query, n_rewrites)

    docs = []
    metas = []

    for query in queries:
        results = query_index(query, collection, n_chunks)
        docs += results["documents"][0]
        metas += results["metadatas"][0]
    
    deduplicated_docs, deduplicated_metas = deduplicate(docs, metas)

    return deduplicated_docs, deduplicated_metas

def deduplicate(docs, metas):
    seen = set()
    out_docs = []
    out_metas = []

    for d, m in zip(docs, metas):
        if d not in seen:
            seen.add(d)
            out_docs.append(d)
            out_metas.append(m)

    return out_docs, out_metas