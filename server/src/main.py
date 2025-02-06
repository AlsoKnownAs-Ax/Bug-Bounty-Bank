from fastapi import FastAPI
from contextlib import asynccontextmanager
from src.database import init_db

app = FastAPI()

@app.get("/")
def read_root():
    return "bug bounty is online"
