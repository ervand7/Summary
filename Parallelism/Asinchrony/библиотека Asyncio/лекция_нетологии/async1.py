# pip install aiohttp
# pip install more-itertools
# В этом модуле представлен код без task'ов. Поэтому сейчас присутствуют 2 проблемы:
# 1) время выполнения chunk'а = времени выполнения самого медленного coroutine
# 2) мы отправляем реквесты только тогда, когда они накопятся в person_data_requests
import asyncio
import time

import aiohttp
from more_itertools import chunked


# ключевое слово async означает, что наша функция будет асинхронной
async def request_people(session, person_id):
    """Создаем корутину для запросов на сервер swapi."""
    # await - это замена yield from из старой версии питона
    response = await session.get(f'http://swapi.dev/api/people/{person_id}')
    return await response.json()


async def main():
    """Событийный цикл."""
    start = time.time()
    person_data_requests = []
    # используем менеджер контекста, чтобы у нас все запросы проходили в одной
    # сессии, а также чтобы сессия завершилась по выходу из контекста
    async with aiohttp.ClientSession() as session:
        for person_id in range(1, 51):
            person_data = request_people(session, person_id)
            # print(person_data)  # coroutine object
            # coroutine - это объект, возвращаемый асинхронной функцией
            # Чтобы coroutine выполнился, нужно либо поставить перед ним await
            # либо вызвать его через asyncio.gather
            person_data_requests.append(person_data)
        # с помощью функции asyncio.gather мы ждем исполнения тасков
        for person_chunk in chunked(person_data_requests, 10):  # отправляем по 10 запросов
            responses = await asyncio.gather(*person_chunk)
            for num, response in enumerate(responses):
                print(num, response)
            print()
    print(time.time() - start)


asyncio.run(main())
