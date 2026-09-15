
import asyncio
import httpx
import logging


logging.basicConfig(
    level=logging.INFO,
    filename="01_Python/Week_4/Day_3/app.log",
    format="%(asctime)s - %(levelname)s - %(name)s - %(message)s"
)

logger = logging.getLogger(__name__)


async def get_data():
    try:
        logger.info("Start fetching data")

        async with httpx.AsyncClient() as client:

            users_task = asyncio.create_task(
                client.get("https://jsonplaceholder.typicode.com/users")
            )

            posts_task = asyncio.create_task(
                client.get("https://jsonplaceholder.typicode.com/posts")
            )

            todos_task = asyncio.create_task(
                client.get("https://jsonplaceholder.typicode.com/todos")
            )

            users, posts, todos = await asyncio.gather(
                users_task,
                posts_task,
                todos_task
            )

            users.raise_for_status()
            posts.raise_for_status()
            todos.raise_for_status()

            result1 = users.json()
            result2 = posts.json()
            result3 = todos.json()

            logger.info("Data fetched successfully")

            return (
                f"Users fetched: {len(result1)}, "
                f"Posts fetched: {len(result2)}, "
                f"Todos fetched: {len(result3)}"
            )

    except httpx.RequestError as error:
        logger.error(f"Request Error: {error}")

    except httpx.HTTPStatusError as error:
        logger.error(f"Status Error: {error}")


async def main():
    result = await get_data()
    print(result)


asyncio.run(main())
