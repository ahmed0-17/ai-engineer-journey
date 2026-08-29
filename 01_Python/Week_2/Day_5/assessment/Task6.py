from typing import TypeVar,Generic

T=TypeVar("T")
class AIResult(Generic[T]):

  def __init__(self,data:T):
    self.data=data


  def get_data(self)->T:
    return self.data




ai_result=AIResult[str]("RAG answer") 
ai_result1=AIResult[float](0.95)

print(ai_result.get_data())
print(ai_result1.get_data())