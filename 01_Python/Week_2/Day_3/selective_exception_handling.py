class SafeContext:

    def __enter__(self):
        print("Started")
        return self

    def __exit__(self, exc_type, exc_value, traceback):

        if exc_type in (ValueError,TypeError) :
            print("ValueError handled:", exc_value)
            return True

        print("Context closed")


with SafeContext():
    # raise ValueError("Invalid value")
    raise TypeError("Invalid datatype")
   


print("Program continues")        