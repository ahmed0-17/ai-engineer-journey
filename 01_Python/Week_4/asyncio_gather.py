import asyncio


async def task1():
    await asyncio.sleep(1)
    return "Task 1 successful"


async def task2():
    await asyncio.sleep(2)
    raise ValueError("Task 2 failed")


async def task3():
    await asyncio.sleep(3)
    return "Task 3 successful"


async def main():

    results = await asyncio.gather(
        task1(),
        task2(),
        task3(),
        return_exceptions=True
    )

    for result in results:

        if isinstance(result, Exception):
            print(f"Error: {result}")
        else:
            print(f"Success: {result}")


asyncio.run(main())