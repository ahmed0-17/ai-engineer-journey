import requests


params={
    "userId":2
}


response=requests.get("https://jsonplaceholder.typicode.com/posts",
                     params=params
                      )


print(response.url)
data=response.json()
print(data)
print(len(data))