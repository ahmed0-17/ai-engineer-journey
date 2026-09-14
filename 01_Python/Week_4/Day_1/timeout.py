import asyncio


async def fetch_data():
    print("Fetching data...")

    await asyncio.sleep(5)

    return "Data received"


async def main():
    try:
        result = await asyncio.wait_for(
            fetch_data(),
            timeout=2
        )

        print(result)

    except asyncio.TimeoutError:
        print("Request took too long")


asyncio.run(main())