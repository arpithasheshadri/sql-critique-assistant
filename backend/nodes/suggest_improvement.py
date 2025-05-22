from langchain_openai import ChatOpenAI
from langchain.prompts import PromptTemplate
from backend.config import api_key
from backend.state import CritiqueState

llm = ChatOpenAI(model="gpt-4", temperature=0.3, openai_api_key=api_key)

def suggest_improvement_node(state: CritiqueState) -> CritiqueState:
    prompt = PromptTemplate.from_template("""
    Based on the following SQL query, rewrite it with improved practices:
    - Use CTEs for complex subqueries
    - Use window functions if appropriate
    - Add table aliases
    - Remove SELECT *
    
    SQL:
    {sql}
    """)
    
    final_prompt = prompt.format(sql=state.sql)
    result = llm.invoke(final_prompt)
    state.suggested_query = result.content.strip()
    return state