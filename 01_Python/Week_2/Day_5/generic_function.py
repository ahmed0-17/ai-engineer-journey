from typing import TypeVar
T=TypeVar("T")

def get_top_result(results:list[T])->T:
    return results[0]


documents = ["Python is...", "RAG is..."]

scores = [0.92, 0.87, 0.81]


print(get_top_result(scores))
print(get_top_result(documents))


