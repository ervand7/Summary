import asyncio

import aiohttp


async def create_user(user_data):
    async with aiohttp.ClientSession() as session:
        async with session.post('http://0.0.0.0:8080/user', json=user_data) as response:
            print(response.status)
            return await response.json()


async def main():
    user = await create_user({'email': 'erdывssывывы7m@ail.ru', 'password_hash': 'asd'})
    print(user)


asyncio.run(main())
