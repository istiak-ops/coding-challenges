from typing import Callable, Any, Dict

def calculate_reward(score: float, multiplier: float = 1.0) -> float:
    """Calculates a reward based on a score and a multiplier."""
    return score * multiplier

def safe_tool_runner(
        tool: Callable, 
        *args: Any,
        metadata: Dict[str, Any] = None, 
        **kwargs: Any
        ) -> Any:
    """
    A production wrapper to execute tools with telemetry.
    
    Args:
        tool: The function to execute.
        *args: Positional arguments for the tool.
        metadata: LLM tracing data (Keyword-only).
        **kwargs: Keyword arguments for the tool.
    """
       
    if metadata is None:
        metadata = {}
    
    print(f"Executing {tool.__name__} with metadata {metadata}")
    return tool(*args, **kwargs)


result = safe_tool_runner(
    calculate_reward, 
    100.0, 
    multiplier=2.5, 
    metadata={"agent_id": "GPT-4"} )
print(f"Result: {result}")
