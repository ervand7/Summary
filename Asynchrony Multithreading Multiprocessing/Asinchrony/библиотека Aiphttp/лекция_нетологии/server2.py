# используем middleware в этом примере
from aiohttp import web


class NotFound(Exception):
    reason = 'Not found'

    def __init__(self, message, *args, **kwargs):
        self.message = message


@web.middleware
async def error_middleware(request, handler):
    try:
        # эта строка - это вызов запроса. Вызов любой функции (привязанной к роуту) на нашем сервере
        response = await handler(request)
        if response.status != 404:
            return response
        message = response.message
    except web.HTTPException as ex:
        if ex.status != 404:
            raise
        message = ex.reason
    return web.json_response({'error': message}, status=404)


async def health(request: web.Request):
    return web.json_response({'status': 'ok'})


app = web.Application(middlewares=[error_middleware])
app.add_routes([web.get('/health', health)])
web.run_app(app, port=8080)
