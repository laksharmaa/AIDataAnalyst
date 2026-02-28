import requests

OLLAMA_URL = "http://localhost:11434/api/generate"

def generate_sql_from_text(user_query: str, schema: str) -> str:

    prompt = f"""
You are a SQL expert.

Database Schema:
{schema}

Rules:
- Only generate SELECT queries.
- Do not generate DELETE, DROP, UPDATE, INSERT.
- Return only SQL query.
- Do not explain anything.

User Query:
{user_query}
"""

    response = requests.post(
        OLLAMA_URL,
        json={
            "model": "llama2",
            "prompt": prompt,
            "stream": False
        }
    )

    result = response.json()
    return result["response"].strip()