# pip install aiohttp
# pip install aiodns  # уксорит работу со службами dns
# pip install cchardet  # уксорит парсинг кодировки
from aiohttp import web

app = web.Application()


async def health(request: web.Request):
    # json_response превращает словарь в json и довешивает все необходимые заголовки
    return web.json_response({'status': 'ok'})


# используем альтернативный вариант работы с роутами
app.add_routes([web.get('/health', health)])
web.run_app(app, port=8080)
