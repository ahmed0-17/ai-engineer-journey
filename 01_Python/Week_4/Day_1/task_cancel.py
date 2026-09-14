import asyncio


async def download():
    try:
        print("Download started")

        await asyncio.sleep(10)

        print("Download finished")

    except asyncio.CancelledError:
        print("Download cancelled")
        raise


async def main():
    task = asyncio.create_task(download())

    await asyncio.sleep(2)

    task.cancel()

    try:
        await task
    except asyncio.CancelledError:
        print("Task stopped")


asyncio.run(main())