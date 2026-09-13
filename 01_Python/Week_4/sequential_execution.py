import asyncio
import time


async def download(name, delay):
    print(f"{name} started")
    await asyncio.sleep(delay)
    print(f"{name} finished")


async def main():
    await download("File 1", 2)
    await download("File 2", 3)


start = time.perf_counter()

asyncio.run(main())

end = time.perf_counter()

print(f"Total time: {end - start:.2f} seconds")