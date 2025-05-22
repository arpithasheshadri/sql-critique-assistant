from langgraph.graph import StateGraph, END
from backend.state import AskState
from backend.nodes.generate_sql import generate_sql_from_question_node
from backend.nodes.parse_query import parse_query_node
from backend.nodes.detect_issues import detect_issues_node
from backend.nodes.suggest_improvement import suggest_improvement_node
from backend.nodes.generate_explanation import generate_explanation_node

def finalize_response_node(state: AskState) -> dict:
    return {
        "generated_sql": state.sql
    }

def run_question_flow(question: str) -> dict:
    builder = StateGraph(AskState)

    builder.add_node("generate_sql", generate_sql_from_question_node)
    builder.add_node("finalize_response", finalize_response_node)

    builder.set_entry_point("generate_sql")
    builder.add_edge("generate_sql", "finalize_response")
    builder.add_edge("finalize_response", END)

    graph = builder.compile()

    initial_state = AskState(question=question)
    return graph.invoke(initial_state)

   
