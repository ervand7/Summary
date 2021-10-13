# вариант исполнения кода с генератором спосков
import asyncio
import time

import aiohttp
from more_itertools import chunked


async def request_people(session, person_id):
    response = await session.get(f'http://swapi.dev/api/people/{person_id}')
    person_data = await response.json()
    return person_data


async def main():
    start = time.time()
    async with aiohttp.ClientSession() as session:
        tasks = [request_people(session, i) for i in range(1, 51)]
        for chunk_of_tasks in chunked(tasks, 10):
            people_chunk = await asyncio.gather(*chunk_of_tasks)
            for num, i in enumerate(people_chunk, 1):
                print(num, i)
            print()
    print(time.time() - start)


asyncio.run(main())
