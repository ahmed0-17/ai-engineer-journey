from functools import wraps

def execution(label):
    def decorator(function):
        @wraps(function)
        def wrapper(*args,**kwargs):
            print(f"[{label}]Start")
            result=function(*args,**kwargs)
            print(f"[{label}]End")
            return result 
        return wrapper    





    return decorator

@execution("RAG")
def retrieve_docs(query,top_k):
    return f"Retrieve {top_k} documents for {query}"


@execution("LLM")
def generate_answer(prompt):
    return f"Answer generated for : {prompt}"




print(retrieve_docs("Python",4))
print(generate_answer("What is RAG?"))