from fastapi import FastAPI, HTTPException
import os
import psycopg2

app = FastAPI()

DATABASE_URL = os.getenv("DATABASE_URL", "postgresql://postgres:postgres@db:5432/postgres")

@app.get("/")
def read_root():
    return {"message": "Hello from Docker and FastAPI via Nginx!"}

@app.get("/health")
def health_check():
    try:
        # Attempt to connect to the PostgreSQL database
        conn = psycopg2.connect(DATABASE_URL)
        conn.close()
        return {"status": "healthy", "database": "connected"}
    except psycopg2.Error:
        raise HTTPException(
            status_code=503,
            detail="Database unavailable"
        )
