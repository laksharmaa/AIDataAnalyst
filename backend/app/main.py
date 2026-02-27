from fastapi import FastAPI
from .database import engine
from . import models

models.Base.metadata.create_all(bind=engine)

app = FastAPI()

@app.get("/")
def root():
    return {"message": "Text-to-SQL backend running"}

from fastapi import Depends
from sqlalchemy.orm import Session
from .database import SessionLocal
from .text_to_sql import generate_sql_from_text

def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()


@app.post("/generate-sql/")
def generate_sql(query: str):
    
    schema = """
    Table: employees
    Columns:
    id (Integer)
    name (String)
    department (String)
    salary (Integer)
    """

    sql_query = generate_sql_from_text(query, schema)

    return {"generated_sql": sql_query}