import requests

OLLAMA_URL = "http://localhost:11434/api/generate"

def generate_sql_from_text(user_query: str, schema: str):
    prompt = f"""
You are a SQL expert.

Database Schema:
{schema}

Convert the following natural language query into SQL:
{user_query}

Only return SQL query.
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
    return result["response"]