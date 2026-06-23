from fastapi import FastAPI
from routes.chat import router

app = FastAPI()

app.include_router(router)

@app.get("/")
def hello_controller():
    return { "message":"Hello Readlyter" }

@app.get("/health")
def health_check():
    return {"status": "ok"}