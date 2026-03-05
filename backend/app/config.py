import os
from dotenv import load_dotenv

load_dotenv()

# Environment variables
DATABASE_URL = os.getenv("DATABASE_URL")
OLLAMA_URL = os.getenv("OLLAMA_URL")
OLLAMA_MODEL = os.getenv("OLLAMA_MODEL")

# Prompt template
SQL_PROMPT_TEMPLATE = """
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