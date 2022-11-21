"""
Здесь скачиваем картинки асинхронным скриптом.
async def нам создает корутину.
Вызов асинхронных функций предваряется инструкцией await. Иначе, вызвав
корутину без await мы получим просто объект корутины.

"""
import asyncio
from time import time

# asyncio не предоставляет API для работы с протоколами http, поэтому используем aiohttp
import aiohttp


# aiohttp не предоставляет нам возможности для асинхронной работы с файлами
# поэтому эта функция у нас будет синхронной
def write_image(data):
    # https://loremflickr.com/cache/resized/65535_51007696125_08cf597744_320_240_nofilter.jpg
    filename = 'file-{}.jpeg'.format(int(time() * 1000))
    with open(f'pictures/{filename}', mode='wb') as file:
        file.write(data)


async def fetch_content(url_address, session):
    """Создадим корутину для получения контента."""
    async with session.get(url_address, allow_redirects=True) as response:
        # метод read() возвращает бинарные данные (картинку)
        data = await response.read()
        write_image(data)


async def main():
    """Создадим корутину для реализации тасок."""
    url = 'https://loremflickr.com/320/240'
    tasks = []
    async with aiohttp.ClientSession() as session:
        for i in range(10):
            # для того, чтобы корутина попала в очередь задач событийного цикла,
            # нужно ее обернуть в экземпляр класса Task с помощью функции create_task
            task = asyncio.create_task(fetch_content(url, session))
            # эти 10 задач нужно где-то хранить. Поэтому добавляем их в список tasks
            tasks.append(task)

        await asyncio.gather(*tasks)


if __name__ == '__main__':
    t0 = time()
    asyncio.run(main())
    print(time() - t0)
