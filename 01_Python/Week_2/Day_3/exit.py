class MyContext:

    def __enter__(self):
        print("Entering context")
        return self

    def __exit__(self, exc_type, exc_value, traceback):
        if exc_type is not None :
         print("Exception Type:", exc_type)
         print("Exception Value:", exc_value)
         print("Traceback:", traceback)
        #  return True     # return true supress(ignore) the exception
        print("Exiting")



with MyContext():
    print("Inside context")
    raise ValueError("Value is wrong")

print("Program coninues ")








