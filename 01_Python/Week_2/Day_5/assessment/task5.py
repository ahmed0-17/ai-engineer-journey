from typing import TypeVar

T=TypeVar("T")


def get_first_result(result:list[T])->T:
   return result[0]


print(get_first_result(["Python","RAG","LLM"]))