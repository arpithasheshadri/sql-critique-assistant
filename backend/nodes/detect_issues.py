from langchain_openai import ChatOpenAI
from langchain.prompts import PromptTemplate
from backend.config import api_key
from backend.state import CritiqueState


llm = ChatOpenAI(model="gpt-4", temperature=0, openai_api_key=api_key)

def detect_issues_node(state: CritiqueState) -> CritiqueState:
    prompt = PromptTemplate.from_template("""
    Review this SQL query and list any issues with performance, readability, or bad practices.
    Focus on:
    - SELECT *
    - Missing WHERE in DELETE/UPDATE
    - Subqueries that can be CTEs
    - Lack of indexes in joins
    - Missing aliases or comments
    
    SQL:
    {sql}
    """)
    
    final_prompt = prompt.format(sql=state.sql)
    result = llm.invoke(final_prompt)
    state.issues = [line.strip("- ") for line in result.content.strip().split("\n") if line.strip()]
    return state