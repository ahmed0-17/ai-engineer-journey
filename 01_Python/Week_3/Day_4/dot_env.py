from dotenv import load_dotenv
import os


load_dotenv()

name=os.getenv("NAME")
age=os.getenv("AGE")
api_key=os.getenv("API_KEY")
app_name=os.getenv("APP_NAME")
debug_status=os.getenv("DEBUG")


# print(name,age)

print(f"API_KEY : {api_key}")
print(f"APP_NAME : {app_name}")
print(f"DEBUG_STATUS : {debug_status}")
# print(type(debug_status))
