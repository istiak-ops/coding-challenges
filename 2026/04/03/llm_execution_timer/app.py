from contextlib import contextmanager
from typing import Iterator
import time

@contextmanager
def track_latency(task_name: str) -> Iterator[None]:
    """Idiomatic Context Manager for LLMOps Telemetry."""
    start_time = time.perf_counter()
    print(f"Starting {task_name}...")
    try:
        yield
    except Exception as e:
        print(f"Error in {task_name}: {type(e).__name__}")
        raise
    finally:
        latency = time.perf_counter() - start_time
        print(f"{task_name} completed in {latency:.2f} seconds.")


try:
    with track_latency("LLM Execution"):
        time.sleep(1.2)
        raise ValueError("Model Hallucination Detected.")
except ValueError:
    print("Main Code: Error Occurred")


       

    

    
