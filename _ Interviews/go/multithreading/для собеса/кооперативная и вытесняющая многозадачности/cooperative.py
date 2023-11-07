# asyncio (Python 3.5+): Python предоставляет библиотеку asyncio для
# асинхронного программирования. Это позволяет использовать кооперативную
# многозадачность для работы с асинхронными функциями без блокировки. Пример:

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
