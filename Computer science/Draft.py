import asyncio


async def foo():
    await asyncio.sleep(5)
    for i in range(5000):
        print(f"Foo: {i}")


async def bar():
    await asyncio.sleep(5)
    for i in range(5000):
        print(f"Bar: {i}")


loop = asyncio.get_event_loop()
loop.run_until_complete(asyncio.gather(foo(), bar()))
