from fastapi import FastAPI, Depends, HTTPException
from sqlalchemy.orm import Session
from sqlalchemy import text
from typing import List

from .database import engine, SessionLocal
from . import models
from .schemas import QueryRequest, QueryResponse
from .text_to_sql import generate_sql_from_text

# Create tables
models.Base.metadata.create_all(bind=engine)

app = FastAPI()

# Dependency
def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()


@app.get("/")
def root():
    return {"message": "Text-to-SQL backend running 🚀"}


@app.post("/query/", response_model=QueryResponse)
def run_text_to_sql(request: QueryRequest, db: Session = Depends(get_db)):

    schema = """
    Table: employees
    Columns:
    id (Integer)
    name (String)
    department (String)
    salary (Integer)
    """

    # 1️⃣ Generate SQL using Llama2
    generated_sql = generate_sql_from_text(request.query, schema)

    # 2️⃣ Basic Safety Check
    if not generated_sql.lower().startswith("select"):
        raise HTTPException(status_code=400, detail="Only SELECT queries allowed")

    try:
        # 3️⃣ Execute SQL safely
        result = db.execute(text(generated_sql))
        rows = result.fetchall()

        # Convert result to list of dicts
        results = [dict(row._mapping) for row in rows]

        return {
            "generated_sql": generated_sql,
            "results": results
        }

    except Exception as e:
        raise HTTPException(status_code=400, detail=str(e))