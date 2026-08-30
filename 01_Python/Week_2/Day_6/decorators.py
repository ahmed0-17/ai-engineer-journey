
def generate_answer():
        print("Generating ai answer")


def add_logging(function):

    def wrapper():
        print("AI function started")

        function()

        print("AI function completed")

    return wrapper

generate_answer=add_logging(generate_answer)

generate_answer()