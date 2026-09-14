import asyncio


async def task1():
    print("Task 1 started")
    await asyncio.sleep(2)
    print("Task 1 finished")


async def task2():
    print("Task 2 started")
    await asyncio.sleep(3)
    print("Task 2 finished")


async def main():
    t1 = asyncio.create_task(task1())
    t2 = asyncio.create_task(task2())

    await t1
    await t2


asyncio.run(main())




# Task 1: ████████████ 2 sec
# Task 2: ██████████████████ 3 sec

# Total ≈ 3 sec