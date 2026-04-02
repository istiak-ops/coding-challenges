from typing import Callable
from functools import wraps

def require_strings(func: Callable) -> Callable:
    @wraps(func)
    def wrapper(*args, **kwargs) -> any:
        for arg in args:
            if not isinstance(arg, str):
                return {
                    "status": "error",
                    "message": "Validation Failed: All arguments must be strings."
                }
        for key, value in kwargs.items():
            if not isinstance(value, str):
                return {
                    "status": "error",
                    "message": f"Validation Failed:{key} must be a string."
                }
        try:
            result = func(*args, **kwargs)
            return result
        except Exception as e:
             return {
             "status": "error",
             "error_type": type(e).__name__,
              "message": str(e)
              }
        finally:
            print(f"validation complete.")
    return wrapper


@require_strings
def concat_tags(tag1, tag2):
    return f"#{tag1} #{tag2}"

# TEST CASES:
print(concat_tags("ai", "python")) # Should work: "#ai #python"
print(concat_tags("ai", 123))      # Should return the Error Dictionary


