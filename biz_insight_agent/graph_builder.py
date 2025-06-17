from langgraph.graph import StateGraph
from typing import TypedDict
from .nodes import input_node, processing_node, recommendation_node


class BizState(TypedDict):
    input_data: dict
    metrics: dict
    recommendations: list


def build_agent_graph():
    builder = StateGraph(state_schema=BizState)

    builder.add_node("input", input_node)
    builder.add_node("process", processing_node)
    builder.add_node("recommend", recommendation_node)

    builder.set_entry_point("input")
    builder.add_edge("input", "process")
    builder.add_edge("process", "recommend")

    return builder.compile()
