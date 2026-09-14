import asyncio

counter = 0
lock=asyncio.Lock()

async def increase():
    global counter

    async with lock:
     current = counter

     await asyncio.sleep(0)

     counter = current + 1


async def main():
    await asyncio.gather(
        increase(),
        increase(),
        increase()
    )

    print(counter)


asyncio.run(main())