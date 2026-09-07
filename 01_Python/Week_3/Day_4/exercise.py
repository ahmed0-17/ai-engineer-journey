import os
from dotenv import load_dotenv

load_dotenv()


app_name = os.getenv("APP_NAME")
debug = os.getenv("DEBUG") == "True"
port = int(os.getenv("PORT", 5000))

print(f"App: {app_name}")
print(f"Debug: {debug}")
print(f"Port: {port}")