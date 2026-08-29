from typing import Literal

def run_agent(mode:Literal["fast","balanced","accurate"])->str:
    return f"Agent mode : {mode}"


print(run_agent("fast"))