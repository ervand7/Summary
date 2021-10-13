# работа с БД через ORM
# pip install gino  # gino - это просто асинхронная надстройка над SQLAlchemy
# pip install bcrypt
# pip install pydantic
# pip install email-validator
import asyncpg
import bcrypt
import pydantic
from aiohttp import web

from db import init_db, User
from errors import NotFound, BadRequest
from validator import UserValidator


@web.middleware
async def error_middleware(request, handler):
    """Перехватчик ошибок."""
    print('Код до вызова метода')
    try:
        response = await handler(request)
    except (NotFound, BadRequest) as er:
        response = web.json_response({'error': er.reason, 'message': er.message}, status=er.status_code)
    except pydantic.error_wrappers.ValidationError as er:
        response = web.json_response({'error': 'Validation error', 'message': er.errors()}, status=422)
    print('Код после вызова метода')
    return response


async def health_view(request: web.Request):
    return web.json_response({'status': 'ok'})


class UserView(web.View):
    """Создадим view через класс"""

    async def get(self):
        user_id = int(self.request.match_info['user_id'])
        user = await User.get(user_id)
        if not user:
            raise NotFound('user not found')
        # to_dict - это метод из gino/crud возвращающий key:value из User
        user_data = user.to_dict()
        # не будем публично показывать людям хеш пароля
        user_data.pop('password_hash')
        return web.json_response(user_data)

    async def post(self):
        # self.request.json() - это корутина
        user_data = await self.request.json()
        user_data_validated = UserValidator(**user_data).dict()
        password_hash = bcrypt.hashpw(user_data_validated.pop('password_hash').encode(), bcrypt.gensalt()).decode()
        user_data_validated['password_hash'] = password_hash
        try:
            # записываем пользователя в бд
            user = await User.create(**user_data_validated)
        except asyncpg.exceptions.UniqueViolationError:
            raise BadRequest('email has already exists')
        user_data = user.to_dict()
        user_data.pop('password_hash')
        return web.json_response(user_data)


app = web.Application(middlewares=[error_middleware])
# таким образом мы добавляем обработчик старта и завершения
# работы с БД (init_db) в приложение
app.cleanup_ctx.append(init_db)
app.add_routes([web.get('/health', health_view)])
app.add_routes([web.post('/user', UserView)])
# здесь мы можем через регулярку передать требование id быть интеджером
app.add_routes([web.get('/user/{user_id:\d+}', UserView)])
web.run_app(app, port=8080)
