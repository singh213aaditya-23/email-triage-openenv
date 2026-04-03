from fastapi import FastAPI
from environment import reset, step

app = FastAPI()

@app.get("/")
def home():
    return {"message": "Email Triage API is running 🚀"}

@app.post("/reset")
def reset_env():
    return reset()

@app.post("/step")
def step_env(action: dict):
    return step(action)