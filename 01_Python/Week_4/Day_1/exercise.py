import asyncio


async def download_file(name, delay):
    print(f"{name} started")

    await asyncio.sleep(delay)

    print(f"{name} finished")


async def main():
 
#  task1=asyncio.create_task(download_file("Avengers Infinity War",2))
#  task2=asyncio.create_task(download_file("Avengers Endgame",3))
#  task3=asyncio.create_task(download_file("Avengers Age of ultron",1))
  

#  await task1
#  await task2
#  await task3    




 results=await asyncio.gather(
   download_file("Avengers Infinity War",2),
   download_file("Avengers Endgame",3),
   download_file("Avengers Age of ultron",1)
 )

 print(results)


asyncio.run(main())