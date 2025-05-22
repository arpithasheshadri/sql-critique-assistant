from fastapi import APIRouter, HTTPException
from pydantic import BaseModel #simple data validation and manipulation
from backend.langgraph_workflow import run_graph
from fastapi.responses import HTMLResponse
from backend.langgraph_question_flow import run_question_flow

router = APIRouter()

class SQLInput(BaseModel):
    sql: str

@router.post("/critique")
async def critique_sql(input_data: SQLInput):
    try:
        result = run_graph(input_data.sql)
        return result
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))

class QuestionInput(BaseModel):
    question: str

@router.post("/ask")
async def ask_question(input_data: QuestionInput):
    try:
        result = run_question_flow(input_data.question)
        return result
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))
    


@router.get("/", response_class=HTMLResponse)
async def root():
    return "<h2>Welcome to the SQL Critique Assistant API</h2><p>Visit <a href='/docs'>/docs</a> to use the API.</p>"
