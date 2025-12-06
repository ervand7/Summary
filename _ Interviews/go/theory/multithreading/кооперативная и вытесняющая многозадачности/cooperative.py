import asyncio

async def task1():
    print("Task 1 starting")
    await asyncio.sleep(1)
    print("Task 1 resuming")

async def task2():
    print("Task 2 starting")
    await asyncio.sleep(1)
    print("Task 2 resuming")

async def main():
    await asyncio.gather(task1(), task2())

asyncio.run(main())