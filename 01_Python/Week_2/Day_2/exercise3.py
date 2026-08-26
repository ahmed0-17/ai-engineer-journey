# Fail_fast_approach

class InvalidModelError(Exception):
     pass


class InvalidTemperatureError(Exception):
        pass

def check_model(model):
     if model not in("gpt","claude","gemini"):
          raise InvalidModelError(f"Unsupported model: {model}")
     return model



def check_temperature(temperature):

    if temperature<0 or temperature>2:
        raise InvalidTemperatureError("Temperature should be maintained between 0C and 2C")

    return temperature    



def create_ai_config(model,temp):
     check_model(model)
     check_temperature(temp)

     return {"model":model,
            "temperature":temp
            }     






try:
   model_info=create_ai_config("gemini",2)
   print(model_info)

except InvalidTemperatureError as error:
     print(error)

     
except InvalidModelError as error:
     print(error)

else:
     print(f"Congratulations for connecting to {model_info['model']} with suitable temperatue {model_info['temperature']}")    

    
finally:
     print("Program Closed")






