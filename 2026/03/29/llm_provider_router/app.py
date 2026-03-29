from typing import Callable, Any, Dict

def call_openai(model: str, temp: float):
    return f"OpenAI logic using {model} at {temp}."

def call_anthropic(prompt: str, max_tokens: int = 100):
    return f"Anthropic logic with {max_tokens} tokens."


def llm_router(provider: Callable, *args: Any, api_key: Dict[str, Any] = "secrets", **kwargs: Any) -> Any:
    """
    A production llm provider router tools with telemetry.
    
    Args:
        Provider: The function to execute.
        *args: Positional arguments for the tool.
        api_key: LLM tracing data (Keyword-only).
        **kwargs: Keyword arguments for the tool.
    """
        
    print(f"Routing to {provider} with API Key: {api_key}")

    if provider == "openai":
        return call_openai(**kwargs)
    elif provider == "anthropic":
        return call_anthropic(*args)
    else:
        return f"Provider {provider} not Supported"
    


# Test OpenAI
print(llm_router("openai", model="gpt-4", temp=0.2)) 

# Test Anthropic
print(llm_router("anthropic", "Analyze this text", 500))