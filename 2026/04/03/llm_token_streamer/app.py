import time
from typing import Iterator


def mock_llm_stream(response_text: str) -> Iterator[str]: 
    split_text = response_text.split()
    for word in split_text:
        yield word
        time.sleep(0.5)


token_stream = mock_llm_stream("Hello World")

for token in token_stream:
    print(token)


