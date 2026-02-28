from pydantic import BaseModel
from typing import List, Any

class QueryRequest(BaseModel):
    query: str

class QueryResponse(BaseModel):
    generated_sql: str
    results: List[Any]