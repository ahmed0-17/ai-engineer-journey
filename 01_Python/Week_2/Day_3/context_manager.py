class MyContext:
    
    def __enter__(self):
        print("Entering context")
        return self

    def __exit__(self, exc_type, exc_value, traceback):
        print("Leaving context")
        



with MyContext():
    print("Inside context")
    raise ValueError("Value is wrong")

