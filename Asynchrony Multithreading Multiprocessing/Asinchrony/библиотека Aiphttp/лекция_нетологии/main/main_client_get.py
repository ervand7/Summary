import asyncio

import aiohttp


async def get_user(user_id):
    async with aiohttp.ClientSession() as session:
        async with session.get(f'http://0.0.0.0:8080/user/{user_id}') as response:
            print(response.status)
            return await response.json()


async def main():
    user = await get_user(32)
    print(user)


asyncio.run(main())
