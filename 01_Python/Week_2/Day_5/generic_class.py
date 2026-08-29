from typing import TypeVar,Generic

T=TypeVar("T")

class Retrieval_result(Generic[T]):

    def __init__(self,data:T):
        self.data=data


    def get_data(self)->T:
     return self.data




retrieved=Retrieval_result[str]("Python is useful for AI")    
retrieved1=Retrieval_result[float](0.94)

print(retrieved.get_data())
print(retrieved1.get_data())