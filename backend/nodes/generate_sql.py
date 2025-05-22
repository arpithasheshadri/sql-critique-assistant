from langchain_openai import ChatOpenAI
from langchain.prompts import PromptTemplate
from backend.state import AskState
from backend.config import api_key

llm = ChatOpenAI(model="gpt-4", temperature=0, openai_api_key=api_key)

def generate_sql_from_question_node(state: AskState) -> AskState:
    if not state.question:
        raise ValueError("Missing question in state")

    prompt = PromptTemplate.from_template("""
    Convert the following natural language question into an SQL query.
    Assume the schema includes common tables like users, orders, products, etc.

    Question:
    {question}
    """)
    final_prompt = prompt.format(question=state.question)
    result = llm.invoke(final_prompt)
    state.sql = result.content.strip()
    return state
