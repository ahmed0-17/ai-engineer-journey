import httpx
import asyncio


async def get_user():
    async with httpx.AsyncClient() as client:
        response=await client.get("https://jsonplaceholder.typicode.com/users/1")
        response.raise_for_status()
        data=response.json()
        print(data['name'])
        print(data['email'])



asyncio.run(get_user())