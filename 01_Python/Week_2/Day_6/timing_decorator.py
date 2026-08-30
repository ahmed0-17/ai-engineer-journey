import time
from functools import wraps
def timing(function):
    @wraps(function)
    def wrapper(*args,**kwargs):
      start=time.time()
      result=function(*args,**kwargs)
      end=time.time()
      print(f"Execution time:{end-start}")

      return result 
    return wrapper  

@timing
def retrieve_document(query ,k_5):
   return f"Retrieve {k_5} documents for {query}"



retrieve=retrieve_document("Python",3)
print(retrieve)
   

    