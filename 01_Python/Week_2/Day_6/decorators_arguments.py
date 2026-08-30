def add_logging(label):

    def decorator(function):

        def wrapper(*args, **kwargs):
            print(f"[{label}] Start")

            result = function(*args, **kwargs)

            print(f"[{label}] End")

            return result

        return wrapper

    return decorator

@add_logging("AI")
def calculate_score(a:int | float ,b:int | float):
    """This function calculates the sum of numbers"""
    return a + b


result=calculate_score(4,5)
print(result)