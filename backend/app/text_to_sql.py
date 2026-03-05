import requests
from .config import OLLAMA_URL, OLLAMA_MODEL, SQL_PROMPT_TEMPLATE


def generate_sql_from_text(user_query: str, schema: str) -> str:

    prompt = SQL_PROMPT_TEMPLATE.format(
        schema=schema,
        user_query=user_query
    )

    response = requests.post(
        OLLAMA_URL,
        json={
            "model": OLLAMA_MODEL,
            "prompt": prompt,
            "stream": False
        }
    )

    result = response.json()
    return result["response"].strip()