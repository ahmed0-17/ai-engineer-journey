import asyncio
import httpx
import time


async def fetch_user(client, user_id):
    url = f"https://jsonplaceholder.typicode.com/users/{user_id}"

    try:
        response = await asyncio.wait_for(
            client.get(url),
            timeout=5
        )

        response.raise_for_status()
                              
        data= response.json()
        return (data["username"],data["email"])

    except asyncio.TimeoutError:
        return f"User {user_id}: Request timed out"

    except httpx.HTTPStatusError as error:
        return f"User {user_id}: HTTP error {error.response.status_code}"

    except httpx.RequestError as error:
        return f"User {user_id}: Request failed - {error}"


async def main():


    async with httpx.AsyncClient() as client:

        results = await asyncio.gather(
            fetch_user(client, 1),
            fetch_user(client, 2),
            fetch_user(client, 3),
            fetch_user(client, 4),
            fetch_user(client, 5),
            return_exceptions=True
        )

        for result in results:
            print(result)




start=time.perf_counter()
asyncio.run(main())
end=time.perf_counter()

print(f"The execution time is : {end-start} secs")