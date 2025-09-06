from fastapi import FastAPI, Query
from agent import ask_agent

app = FastAPI()

@app.get("/ask")
def ask(prompt: str = Query(..., description="Tu pregunta")):
    response = ask_agent(prompt)
    return {"respuesta": response}