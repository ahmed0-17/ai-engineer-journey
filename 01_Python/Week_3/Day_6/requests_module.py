import requests

response=requests.get("https://youtube.com")

print(response)
print(response.status_code)
print(response.text)