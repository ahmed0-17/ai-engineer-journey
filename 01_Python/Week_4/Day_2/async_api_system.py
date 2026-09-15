import asyncio
import httpx


async def producer(queue):
    for i in range(1,6): 
     await queue.put(i)
     print(f"ID {i} produced")
  


async def consumer(queue, client, semaphore):
 while True:
    user_id=await queue.get()
    try:
      async with semaphore:    
        print(f"Consumed: {user_id}")
        response=await asyncio.wait_for(
        client.get(f"https://jsonplaceholder.typicode.com/users/{user_id}"),
         timeout=5
       )
        response.raise_for_status()
        data=response.json()
        print(data["username"],data["email"])
    
       

    except httpx.RequestError as error:
       print(f"Request Error: {error}")

    
    except httpx.HTTPStatusError as error:
       print(f"Status Error {error}")
   
    finally:
        queue.task_done()


async def main():
    queue = asyncio.Queue()
    semaphore = asyncio.Semaphore(2)

    async with httpx.AsyncClient() as client:

        producer_task=asyncio.create_task(producer(queue))
        consumer_task1=asyncio.create_task(consumer(queue,client,semaphore))
        consumer_task2=asyncio.create_task(consumer(queue,client,semaphore))
        await producer_task
        await queue.join()
        consumer_task1.cancel()
        consumer_task2.cancel()


asyncio.run(main())