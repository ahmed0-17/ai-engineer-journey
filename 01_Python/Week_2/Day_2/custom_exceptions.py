class InvalidModelError(Exception):
     pass



def check_model(model):
     if model not in("gpt","claude","gemini"):
          raise InvalidModelError(f"Unsupported model: {model}")
     return model



try:
    model= check_model("grok")
    print(model)

except InvalidModelError as error:
     print(error)





#InvalidTemperatureError custom Exception


class InvalidTemperatureError(Exception):
        pass

    

def set_temperature(temperature):

    if temperature<0 or temperature>2:
        raise InvalidTemperatureError("Temperature should be maintained between 0C and 2C")

    return temperature    


try:
    temperature=set_temperature(3)
    print(temperature)
except InvalidTemperatureError as error:
    print(error)    