def greetings(username:str | None)->str:
    if username is None:
        return "Hello guest"

    return f"Hello {username}"


print(greetings("Ahmed"))
print(greetings(None))