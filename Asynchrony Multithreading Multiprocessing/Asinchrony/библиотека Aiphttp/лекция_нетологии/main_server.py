# работа с БД через ORM
# pip install gino  # gino - это просто асинхронная надстройка над SQLAlchemy
# pip install bcrypt
# pip install pydantic
# pip install email-validator
import asyncpg
import bcrypt
import pydantic
from aiohttp import web
from gino import Gino
from pydantic import BaseModel, EmailStr

DSN = 'postgres://lesson_aiohttp:lesson_aiohttp@localhost:5432/lesson_aiohttp'
db = Gino()


class User(db.Model):
    __tablename__ = 'test_app_users'

    id = db.Column(db.Integer(), primary_key=True)
    email = db.Column(db.String(128), nullable=False)
    password_hash = db.Column(db.String(256), nullable=False)

    # прописываем индекс, чтобы ускорить поиск по БД
    _idx_email = db.Index('test_app_users_email', 'email', unique=True)


class UserValidator(BaseModel):
    """Используем для разнообразия не json-схему, а pydantic."""
    email: EmailStr
    password_hash: str


async def init_db(application):
    """Инициализируем БД"""
    # вначале приложения
    print('Приложение стартовало')
    await db.set_bind(DSN)
    await db.gino.create_all()  # создание всех таблиц
    yield
    # вконце приложения
    await db.pop_bind().close()  # разрыв связи с БД
    print('Приложение завершило работу')


class HttpException(Exception):

    def __init__(self, message, *args, **kwargs):
        self.message = message


class NotFound(HttpException):
    reason = 'Not found'
    status_code = 404


class BadRequest(HttpException):
    reason = 'Bad Request'
    status_code = 400


@web.middleware
async def error_middleware(request, handler):
    print('Код до вызова метода')
    try:
        response = await handler(request)
    except (NotFound, BadRequest) as er:
        response = web.json_response({'error': er.reason, 'message': er.message}, status=er.status_code)
    except pydantic.error_wrappers.ValidationError as er:
        response = web.json_response({'error': 'Validation error', 'message': er.errors()}, status=422)
    print('Код после вызова метода')
    return response


async def health(request: web.Request):
    return web.json_response({'status': 'ok'})


class UserView(web.View):
    """Создадим view через класс"""

    async def get(self):
        user_id = int(self.request.match_info['user_id'])
        user = await User.get(user_id)
        if not user:
            raise NotFound('user not found')
        user_data = user.to_dict()
        user_data.pop('password_hash')
        return web.json_response(user_data)

    async def post(self):
        # self.request.json() - это корутина
        user_data = await self.request.json()
        user_data_validated = UserValidator(**user_data).dict()
        password_hash = bcrypt.hashpw(user_data_validated.pop('password_hash').encode(), bcrypt.gensalt()).decode()
        user_data_validated['password_hash'] = password_hash
        try:
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
app.add_routes([web.get('/health', health)])
app.add_routes([web.post('/user', UserView)])
app.add_routes([web.get('/user/{user_id:\d+}', UserView)])
web.run_app(app, port=8080)
