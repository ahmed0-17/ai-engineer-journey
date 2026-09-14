import asyncio

semaphore = asyncio.Semaphore(2)


async def download(name):
    async with semaphore:
        print(f"{name} started")

        await asyncio.sleep(3)

        print(f"{name} finished")


async def main():
    await asyncio.gather(
        download("File 1"),
        download("File 2"),
        download("File 3"),
        download("File 4"),
    )


asyncio.run(main())