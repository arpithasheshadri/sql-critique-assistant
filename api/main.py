from fastapi import FastAPI
from api.routes import router

app = FastAPI(
    title="SQL Critique Assistant",
    description="Critiques and improves SQL queries using LangGraph and LLMs",
    version="1.0.0"
)

app.include_router(router)