import asyncio


async def sleep(seconds: int) -> None:
    await asyncio.sleep(seconds)
    print(f"sleep {seconds}s")


# 3.10
async def old_main():
    tasks = []
    for s in [2, 2, 2, 2, 2, 2, 2]:
        tasks.append(asyncio.create_task(sleep(s)))
    await asyncio.gather(*tasks)


# 3.11
async def main():
    async with asyncio.TaskGroup() as tg:
        for s in [2, 2, 2, 2, 2, 2, 2]:
            tg.create_task(sleep(s))


asyncio.run(main())
