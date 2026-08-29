# RAG API response
from typing import TypeVar,Generic

T=TypeVar("T")

class RAGResponse(Generic[T]):

    def __init__(self ,success:bool,data:T):
        self.success=success
        self.data=data


    def get_data(self)->T:
        return self.data



rag_response1=RAGResponse[str](True,"RAG answer generted successfully")
rag_response2=RAGResponse[list[str]](True,["Python document", "RAG document", "LLM document"])
print(rag_response1.get_data())
print(rag_response2.get_data())
