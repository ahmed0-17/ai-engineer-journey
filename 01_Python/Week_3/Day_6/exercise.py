import requests


response=requests.get("https://dog.ceo/api/breeds/image/random")

data=response.json()

print(response.status_code)
print(data['message'])