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
    except Exception as e:
        raise HTTPException(status_code=500, detail=f"Database unhealthy: {str(e)}")
