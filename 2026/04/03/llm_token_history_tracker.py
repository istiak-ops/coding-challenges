from typing import Callable, Dict

def create_agent_tracker() -> Callable:
    total_token = 0
    prompt_history = []
    def log_interaction(prompt_text: str, tokens_used: int) ->Dict:
        nonlocal total_token
        total_token += tokens_used
        prompt_history.append((prompt_text))
        return {"total_tokens": total_token, "prompt_history": prompt_history}
    return log_interaction


# initialize the agent tracker
agent_tracker = create_agent_tracker()
print(agent_tracker("hello", 10)) # Should
print(agent_tracker("world", 20))
print(agent_tracker("python", 30))

