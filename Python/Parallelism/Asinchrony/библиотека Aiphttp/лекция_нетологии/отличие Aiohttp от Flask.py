# описание клиентской части
import aiohttp

async with aiohttp.ClientSession() as session:  # создаем сессию
    async with session.get('http://httpbin.org/get') as resp:  # отправляем запрос
        await resp.text()  # ожидаем текстовое представление ответа

# _____________________________________________________________________________
# описание серверной части
from aiohttp import web

# определение роутера
routes = web.RouteTableDef()


@routes.get('/')
# в отличие от Flask, тут переменная не подставляется в функцию
# она падает в объект request
# Объект request не импортируется, а подставляется в качестве переменной
async def hello(request):
    return web.Response(text="Hello, world")


@routes.get('/{name}')
async def hello_name(request):
    name = request.match_info['name']
    return web.Response(text=f"Hello, {name}")


@routes.get(r'/1/{name:\d+}')
async def hello_name_regexp(request):
    name = request.match_info['name']
    return web.Response(text=f"buy, {name}")


# создание самого приложения (инстанс сервера)
app = web.Application()
app.add_routes(routes)
web.run_app(app)
# _____________________________________________________________________________
# Если мы не хотим отдельно создавать роуты и объявлять их через декораторы,
# мы можем добавить их альтернативным методом
app.add_routes([web.get('/path1', hello),
                web.post('/path2', hello_name),
                web.get('/path3', hello_name_regexp),
                ])


# _____________________________________________________________________________
# Как и в случае с Flask и DRF, мы можем делать класс view
@routes.view('/{name}')
class NameView(web.View):
    async def get(self):
        name = self.request.match_info['name']
        return web.Response(text=f"Hello, {name}")


# _____________________________________________________________________________
# Как и в джанго, мы можем делать middleware
# middleware - это код, который будет выполняться во время каждого запроса
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


app = web.Application(middlewares=[error_middleware])
