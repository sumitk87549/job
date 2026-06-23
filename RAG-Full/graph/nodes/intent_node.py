from graph.state import GraphState

def detect_intent(state: GraphState):
    query = state["query"].lower()

    if "summary" in query or "summate" in query or "summarize" in query:
        return {"intent":"summary"}
    elif "translate" in query or "translated" in query:
        return {'intent': 'translate'}
    else:
        return {'intent':'qa'}