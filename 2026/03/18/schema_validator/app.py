from typing import List, Dict


def validate_agent_output(output: Dict, required_keys: List[str]) -> bool:
    """schema validation to check for required keys"""
    if not output:
        return False
    
    for key in required_keys:
        if key not in output:
            return False
    return True
