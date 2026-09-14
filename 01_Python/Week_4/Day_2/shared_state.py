import asyncio

counter = 0


async def increase():
    global counter

   
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