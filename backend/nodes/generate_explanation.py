from langchain_openai import ChatOpenAI
from langchain.prompts import PromptTemplate
from backend.config import api_key
from backend.state import CritiqueState

llm = ChatOpenAI(model="gpt-4", temperature=0.3, openai_api_key=api_key)

def generate_explanation_node(state: CritiqueState) -> CritiqueState:
    prompt = PromptTemplate.from_template("""
    Explain in plain English:
    1. What this SQL query is doing
    2. Why the suggested improvements are better
    3. When to use CTEs or window functions
    
    Original SQL:
    {sql}
    
    Suggested SQL:
    {suggested}
    """)
    
    final_prompt = prompt.format(sql=state.sql, suggested=state.suggested_query)
    result = llm.invoke(final_prompt)
    state.explanation = result.content.strip()
    return state