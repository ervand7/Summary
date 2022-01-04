import aiohttp
import asyncio

HOST = 'http://0.0.0.0:8080'


async def make_request(path, method='get', **kwargs):
    async with aiohttp.ClientSession() as session:
        request_method = getattr(session, method)
        async with request_method(f'{HOST}/{path}', **kwargs) as response:
            return (await response.json())


async def main():
    # response = await make_request('user', 'post', json={'username': 'nikitos4', 'password': 'qwe'})
    # print(response)
    response = await make_request('user/1', 'get')
    print(response)


asyncio.run(main())