import requests

payload={
    "title":"My first api",
    "body":"I am learning Python HTTP  requests",
    "userId":5
}


response=requests.post("https://jsonplaceholder.typicode.com/posts",
                       json=payload
                       )


result=response.json()
print(response.status_code)
print(result)
print(result['userId'])