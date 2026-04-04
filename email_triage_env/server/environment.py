from server.grader import grade_easy

state = {"email": "Test email", "true": {"type": "spam"}}

def reset():
    return state

def step(action):
    reward = grade_easy(action, state["true"])
    return {"reward": reward, "done": True}