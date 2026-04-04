from fastapi import FastAPI
from server.environment import reset, step

app = FastAPI()

@app.post("/reset")
def reset_env():
    return reset()

@app.post("/step")
def step_env(action: dict):
    return step(action)