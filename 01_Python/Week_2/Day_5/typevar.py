from typing import TypeVar
#Constrained TypeVar
T = TypeVar("T", int, float)
def double(value: T) -> T:
    return value * 2



