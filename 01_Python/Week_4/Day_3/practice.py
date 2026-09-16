import asyncio
import time


async def work(name, seconds):
    print(f"{name} started")
    await asyncio.sleep(seconds)
    print(f"{name} finished")




# functions run synchronously
# async def main():

#  await work("Task1",3)
#  await work("Task2",3)



# asyncio.run(main())


# functions run concurrently
async def main():
   start=time.perf_counter()
#  task1 = asyncio.create_task(work("Task1", 3))
#  task2 = asyncio.create_task(work("Task2", 3))

#  await asyncio.gather(task1, task2)

   results = await asyncio.gather(
        work("Task1", 3),
        work("Task2", 3)
    )

   end=time.perf_counter()
   print(f"The execution time is : {end-start:.2f}s")


asyncio.run(main()) 