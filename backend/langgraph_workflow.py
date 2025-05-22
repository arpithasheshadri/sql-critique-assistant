# backend/langgraph_workflow.py

from langgraph.graph import StateGraph, END
from backend.state import CritiqueState
from backend.nodes.parse_query import parse_query_node
from backend.nodes.detect_issues import detect_issues_node
from backend.nodes.suggest_improvement import suggest_improvement_node
from backend.nodes.generate_explanation import generate_explanation_node

def finalize_response_node(state: CritiqueState) -> dict:
    state.final_response = {
        "parsed": state.parsed,
        "issues": state.issues,
        "suggested_query": state.suggested_query,
        "explanation": state.explanation
    }
    return state

def run_graph(sql: str) -> dict:
    builder = StateGraph(CritiqueState)

    builder.add_node("parse_query", parse_query_node)
    builder.add_node("detect_issues", detect_issues_node)
    builder.add_node("suggest_improvement", suggest_improvement_node)
    builder.add_node("generate_explanation", generate_explanation_node)
    builder.add_node("finalize_response", finalize_response_node)

    builder.set_entry_point("parse_query")
    builder.add_edge("parse_query", "detect_issues")
    builder.add_edge("detect_issues", "suggest_improvement")
    builder.add_edge("suggest_improvement", "generate_explanation")
    builder.add_edge("generate_explanation", "finalize_response")
    builder.add_edge("finalize_response", END)

    graph = builder.compile()

    initial_state = CritiqueState(sql=sql)

    final_state = graph.invoke(initial_state)
    return final_state