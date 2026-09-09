import httpx

headers={
    "Accept":"application/json",
    "User-Agent":"MyPythonApp"
}

payload={
    "title":"httpx request",
    "body":"Sending request through httpx library synchronusly",
    "userId" :1
}

try:
 response=httpx.post("https://jsonplaceholder.typicode.com/posts",
                headers=headers,
                json=payload,
                timeout=5
                   )
 response.raise_for_status()
 result=response.json()

 print(result)
 print(response.status_code)

except httpx.HTTPStatusError as error: 
 print(f"Error : {error}")

except httpx.RequestError as error:
    print("Request failed:", error) 
 