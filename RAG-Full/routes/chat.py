from fastapi import APIRouter
from entities.ChatRequest import ChatRequest
from graph.rag_graph import RAGGraph
from services.chat_service import process_chat
router = APIRouter()

@router.post("/chat")
def chat(request: ChatRequest):
    return process_chat(request)

