"""Работа с таском."""
import asyncio
import time

import aiohttp
from more_itertools import chunked


async def request_people(session, person_id):
    response = await session.get(f'http://swapi.dev/api/people/{person_id}')
    # можем посмотреть, в каком порядке у нас готовятся респонсы
    person_data = await response.json()
    # видим, что запросы идут в хаотичном порядке
    print(person_data)
    return person_data


async def main():
    start = time.time()
    tasks = []
    async with aiohttp.ClientSession() as session:
        for person_id in range(1, 50):
            person_data = request_people(session, person_id)
            # тут мы используем task для того, чтобы запросы начали уже идти
            # не дожидаясь того, что person_data_requests заполнится до конца
            # asyncio.create_task принимает в качестве аргемента корутину
            task = asyncio.create_task(person_data)
            tasks.append(task)
        for person_chunk in chunked(tasks, 10):
            responses = await asyncio.gather(*person_chunk)
            print()

    print(time.time() - start)


asyncio.run(main())
