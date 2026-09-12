import asyncio


async def download_file(name, delay):
    print(f"{name} started")

    await asyncio.sleep(delay)

    print(f"{name} finished")


async def main():

 task1=asyncio.create_task(download_file("Avengers Infinity War",2))
 task2=asyncio.create_task(download_file("Avengers Infinity Endgame",3))
  

 await task1
 await task2
    


asyncio.run(main())