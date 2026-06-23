from langgraph.graph import StateGraph, END

from .state import GraphState
from graph.nodes.intent_node import detect_intent
from graph.nodes.response_node import response_node

builder = StateGraph(GraphState)

builder.add_node("intent", detect_intent)
builder.add_node("response", response_node)

builder.set_entry_point("intent")

builder.add_edge("intent","response")
builder.add_edge("response", END)

RAGGraph = builder.compile()