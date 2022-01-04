import asyncio

import aiohttp


async def check_health():
    async with aiohttp.ClientSession() as session:
        # отправим запрос на несуществующий адрес, потестируем middleware
        async with session.get('http://0.0.0.0:8080/non_exists') as response:
            print(response.status)
            return await response.json()


async def main():
    health = await check_health()
    print(health)


asyncio.run(main())
