import requests


headers={
    "Accept":"application/json",
    "User-Agent":"MyPythonApp"
}


response=requests.get("https://jsonplaceholder.typicode.com/posts",
                     headers=headers
                      )

data=response.json()

print(response.status_code)
print(len(data))