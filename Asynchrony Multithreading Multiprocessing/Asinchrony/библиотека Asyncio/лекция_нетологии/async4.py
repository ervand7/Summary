"""
Здесь расписан асинхронный вариант sync2.py.
Прорабатываем генераторы.
"""

import asyncio

import aiohttp
from more_itertools import chunked


async def request_to_server(session, person_id):
    response = await session.get(f'http://swapi.dev/api/people/{person_id}')
    person_data = await response.json()
    return person_data


async def request_people(session, n):
    size = n // 5 or 1
    for chunk in chunked(range(1, n), size):
        tasks = [request_to_server(session, i) for i in chunk]
        ready_peoples = await asyncio.gather(*tasks)
        for people in ready_peoples:
            yield people
        print()


async def main():
    async with aiohttp.ClientSession() as session:
        async for person in request_people(session, 51):
            print(person)


asyncio.run(main())
