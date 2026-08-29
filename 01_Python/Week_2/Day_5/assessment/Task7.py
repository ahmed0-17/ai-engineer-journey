from typing import TypeVar

T=TypeVar("T",int,float)

def normalize_score(score:T)->T:
    return score



print(normalize_score(99.8))
print(normalize_score(100))
