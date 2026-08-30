#decorators with ar~guments
def add_logging(function):

    def wrapper(*args,**kwargs):
        print("Start")
        function(*args,**kwargs)
        print("End")
    return wrapper

@add_logging
def generate_answer(prompt):
    print(f"LLM:{prompt}")



@add_logging
def generate_embeddings():
    print("Generating embedding.....")



@add_logging
def search_document(query,top_k):
      print(f"Query: {query}, Top K: {top_k}")





generate_answer("What is RAG")
search_document("Python",5)
