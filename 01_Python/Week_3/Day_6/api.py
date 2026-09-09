import requests

response = requests.get("https://jsonplaceholder.typicode.com/users/1")

print(response.status_code)

data = response.json()

print(data['address']['street'])
print(data['email'])