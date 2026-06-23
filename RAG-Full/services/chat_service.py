from graph.rag_graph import RAGGraph

def process_chat(request):
    result = RAGGraph.invoke(request)
    return result