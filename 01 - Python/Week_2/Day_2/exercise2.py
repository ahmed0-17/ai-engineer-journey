

# from exception handling


def set_temperature(temperature):

    if temperature<0 or temperature>2:
        raise ValueError("Temperature should be maintained between 0C and 2C")

    return temperature    


try:
    temperature=set_temperature(3)
    print(temperature)
except ValueError as error:
    print(error)    



