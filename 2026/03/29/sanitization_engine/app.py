from typing import Callable, Any, Dict

def clean_whitespace(text: str) -> str:
    return text.strip()

def redact_terms(text: str, *terms: str) -> str:
    for term in terms:
        text = text.replace(term, "[REDACTED]")
    return text


def execute_pipeline(tool: Callable, text: str, *args: Any, **kwargs: Any) -> Any:
    """ DoctString """

    return tool(text, *args, **kwargs)


print(execute_pipeline(redact_terms, "admin@company.com", "admin", "company"))
print(execute_pipeline(clean_whitespace, " hello world "))