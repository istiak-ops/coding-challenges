from functools import wraps
from typing import Callable, Any

def spy(func: Callable) -> Callable:
    @wraps(func)
    def wrapper(*args: Any, **kwargs: Any) -> Any:
        print(f"Logging: checking {func.__name__}")
        return func(*args, **kwargs)
    return wrapper

@spy
def secret_vault(items: str) -> str:
    return f"The secret items in vault is {items}"

print(secret_vault("gold"))
print(secret_vault.__name__)