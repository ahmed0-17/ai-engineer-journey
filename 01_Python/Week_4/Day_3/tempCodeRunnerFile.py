import asyncio

async def work(name, seconds):
    print(f"{name} started")
    await asyncio.sleep(seconds)
    print(f"{name} finished")


async def main():

 await work("Task1",3)
 await work("Task2",3)
