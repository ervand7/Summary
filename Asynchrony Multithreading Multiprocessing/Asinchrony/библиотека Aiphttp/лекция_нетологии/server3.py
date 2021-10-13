# работа с БД без алхимии
# pip install asyncpg
from aiohttp import web
import asyncpg

DSN = 'postgres://lesson_aiohttp:lesson_aiohttp@localhost:5432/lesson_aiohttp'


# этот обработчик должен обязательным параметром принимать приложение
async def init_db(application):
    """
    Функция для инициализации БД.
    У нас есть необходимость в установлении и разрыве связи с БД.
    То, что мы пропишем до yield - выполнится в начале приложения,
    а все остальное - при завершении приложения.
    """
    print('Приложение стартовало')
    conn = await asyncpg.connect(DSN)
    # делаем так, чтобы все наши роуты видели это подключение
    application['pg_con'] = conn
    yield
    await conn.close()
    print('Приложение завершило работу')


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
    # делаем запрос к БД
    connection: asyncpg.Connection = request.app['pg_con']
    result = await connection.fetchval('SELECT 1')
    return web.json_response({'status': 'ok', 'pg_test': result})


app = web.Application(middlewares=[error_middleware])
# таким образом мы добавляем обработчик старта и завершения
# работы с БД (init_db) в приложение
app.cleanup_ctx.append(init_db)
app.add_routes([web.get('/health', health)])
web.run_app(app, port=8080)
