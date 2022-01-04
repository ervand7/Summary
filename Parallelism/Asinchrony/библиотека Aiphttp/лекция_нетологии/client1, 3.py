import asyncio

import aiohttp


async def check_health():
    async with aiohttp.ClientSession() as session:
        async with session.get('http://0.0.0.0:8080/health') as response:
            print(response.status)
            return await response.json()


async def main():
    health = await check_health()
    print(health)


asyncio.run(main())
