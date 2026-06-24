from fastapi import FastAPI
from backend.app.api.health import router as health_router

app = FastAPI()
app.include_router(health_router)

@app.get("/")
def root_endpoint():
    return {
  "service": "Readlyte RAG",
  "status": "running"
}