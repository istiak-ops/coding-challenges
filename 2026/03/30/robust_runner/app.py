from functools import wraps
from typing import Callable, Any, Dict

def robust_tool(func: Callable) -> Callable:
    @wraps(func)
    def wrapper(*args: Any, **kwargs: Any) -> Any:
        print(f"Running {func.__name__}")
        try:
            result = func(*args, **kwargs)
            return result
        except Exception as e:
            return {
                "status": "fail", 
                "error_type": type(e).__name__, 
                "message": str(e)
                }
        finally:
            print(f"Registry sync complete")
    return wrapper

@robust_tool
def divider(a: float, b:float) -> float:
    return a / b

print(divider(10, 2)) 
print()  # Should return 5.0
print(divider(10, 0))   # Should return a failure dictionary
print()
print(divider(10, "a")) # Should return a failure dictionary