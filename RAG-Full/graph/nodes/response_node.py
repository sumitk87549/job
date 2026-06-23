from graph.state import GraphState

def response_node(state: GraphState):
    intent = state['intent']
    return {'answer': f"Intent detected: {intent}"}

