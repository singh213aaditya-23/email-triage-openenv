from server .grader import grade_easy, grade_medium, grade_hard

state = {}

def reset():
    global state
    state = {
        "email": "Reset your password urgently.",
        "true": {"type": "security", "priority": "high", "route": "security_team"}
    }
    return state


def step(action):
    true = state["true"]

    return {
        "easy": grade_easy(action, true),
        "medium": grade_medium(action, true),
        "hard": grade_hard(action, true),
    }