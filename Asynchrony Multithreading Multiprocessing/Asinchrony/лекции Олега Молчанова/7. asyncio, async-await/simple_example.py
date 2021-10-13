import asyncio

"""
Начиная с версии python 3.5:
 - yield from заменен на await
 - asyncio.coroutine заменен на async def
 - ensure_future заменен на create_task

if __name__ == '__main__': 
    loop = asyncio.get_event_loop()
    loop.run_until_complete(main()) 
    loop.close()
все это заменено на     
if __name__ == '__main__':
    asyncio.run(main())
"""


async def print_nums():
    num = 1
    while True:
        print(num)
        num += 1
        await asyncio.sleep(1)


async def print_time():
    count = 0
    while True:
        if count % 3 == 0:
            print('{} seconds have passed'.format(count))
        count += 1
        await asyncio.sleep(0.6)


async def main():
    """Event loop. Это тоже будет корутиной, как и print_nums и print_time."""
    # create_task обеспечивает создание объекта будущего
    # она нужна для создания очереди
    task1 = asyncio.create_task(print_nums())
    task2 = asyncio.create_task(print_time())

    # gather - тоже генератор, помогает нам дождаться результата переданных в него тасков
    await asyncio.gather(task1, task2)


if __name__ == '__main__':
    asyncio.run(main())
