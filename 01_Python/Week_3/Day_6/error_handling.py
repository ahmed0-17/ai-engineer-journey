import requests


try:

 response=requests.get("https://jsonplaceholder.typicode.com/users/1",
                       timeout=5
                       )

 response.raise_for_status()

 result=response.json()

 print(result) 


except requests.RequestException as error:
 print("Error : ", error)
 