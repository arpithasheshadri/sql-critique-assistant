from langchain_openai import ChatOpenAI
from langchain.prompts import PromptTemplate
from backend.config import api_key
from backend.state import CritiqueState

llm = ChatOpenAI(model="gpt-4", temperature=0, openai_api_key=api_key)

def parse_query_node(state: CritiqueState) -> CritiqueState:
    prompt = PromptTemplate.from_template("""
    Analyze the following SQL query and break it down into components:
    - SELECT clause
    - FROM clause
    - WHERE clause (if any)
    - GROUP BY or HAVING clause
    - JOINs (if any)
    
    SQL:
    {sql}
    """)
    
    final_prompt = prompt.format(sql=state.sql)
    result = llm.invoke(final_prompt)

    state.parsed = result.content.strip()
    return state