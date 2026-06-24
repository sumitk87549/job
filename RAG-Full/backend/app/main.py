from fastapi import FastAPI
app = FastAPI()

@app.get("/")
def enter():
    return {
  "service": "Readlyte RAG",
  "status": "running"
}