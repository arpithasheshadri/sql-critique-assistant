# backend/state.py

from typing import List, Dict, Optional
from pydantic import BaseModel

class CritiqueState(BaseModel):
    question: Optional[str] = None
    sql: Optional[str] = None
    parsed: str = ""
    issues: List[str] = []
    suggested_query: str = ""
    explanation: str = ""
    final_response: Dict = {}

class AskState(BaseModel):
    question: str
    sql: Optional[str] = None

