import asyncio


async def producer(queue):
    for i in range(5):
        await queue.put(i)
        print(f"Produced: {i}")

        await asyncio.sleep(1)


async def consumer(queue):
    while True:
        item = await queue.get()

        print(f"Consumed: {item}")

        await asyncio.sleep(2)

        queue.task_done()


async def main():
    queue = asyncio.Queue()

    producer_task = asyncio.create_task(
        producer(queue)
    )

    consumer_task = asyncio.create_task(
        consumer(queue)
    )

    await producer_task

    await queue.join()

    consumer_task.cancel()


asyncio.run(main())