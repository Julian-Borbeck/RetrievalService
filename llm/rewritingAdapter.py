import json
import requests
from settings import settings

def rewrite_query_k_times(user_query, k = 5):
    
    schema = {
        "type": "object",
        "properties": {
            "queries": {
                "type": "array",
                "items": {"type": "string"},
                "minItems": k,
                "maxItems": k,
            }
        },
        "required": ["queries"],
        "additionalProperties": False,
    }

    system = (
            "You rewrite user queries for semantic retrieval. \n"
            "The focus of your retrieval is Multiple Sequence Alignment commands, the goal is to find documents that help the user construct commands for Multiple Sequence Alignment with MUSCLE, MAFFT, Clustal.\n"
            "Rules:\n"
            f"- Produce exactly {k} rewritten queries.\n"
            "- Keep meaning identical to the user query.\n"
            "- Remove chatty filler. Keep it search-friendly.\n"
            "- Each rewrite should differ in phrasing / keywords.\n"
            "- Do NOT add new constraints or facts.\n"
            "- Output must match the provided JSON schema exactly."
        )
    

    payload = {
        "model": settings.model_rewrite,
        "stream": False,
        "format": schema,
        "messages": [
            {"role": "system", "content": system},
            {"role": "user", "content": user_query},
        ],
        "options": {
            "temperature": 0.4,
        },
    }

    r = requests.post(f"{settings.ollama_url}/api/chat", json=payload, timeout=60)
    r.raise_for_status()

    content = r.json()["message"]["content"]
    data = json.loads(content)

    out = []
    seen = set()
    for q in data["queries"]:
        q2 = " ".join(q.split())
        if q2 and q2 not in seen:
            seen.add(q2)
            out.append(q2)

    return out[:k]