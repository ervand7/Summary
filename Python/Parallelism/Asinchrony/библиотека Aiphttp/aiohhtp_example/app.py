import pydantic
import hashlib
import asyncpg
from gino import Gino
from aiohttp import web

PG_DSN = f'postgres://lesson_aiohttp:lesson_aiohttp@127.0.0.1:5432/aiohttp_netology_example'


@web.middleware
async def validation_error_handler(request, handler):
    try:
        response = await handler(request)
    except pydantic.error_wrappers.ValidationError as er:
        response = web.json_response({'error': str(er)}, status=400)
    return response

app = web.Application(middlewares=[validation_error_handler])
db = Gino()


class ModelMixin:

    @classmethod
    async def create_instance(cls, *args, **kwargs):
        try:
            return (await cls.create(*args, **kwargs))
        except asyncpg.exceptions.UniqueViolationError:
            raise web.HTTPBadRequest


class UserModel(db.Model, ModelMixin):

    __tablename__  = 'app_users'

    id = db.Column(db.Integer(), primary_key=True)
    username = db.Column(db.String(), nullable=False)
    password = db.Column(db.String(), nullable=False)

    _idx1 = db.Index('app_users_username', 'username', unique=True)

    @classmethod
    async def create_instance(cls, *args, **kwargs):
        kwargs['password'] = hashlib.md5(kwargs['password'].encode()).hexdigest()
        return (await super().create_instance(*args, **kwargs))

    def to_dict(self):
        user_data = super().to_dict()
        user_data.pop('password')
        return user_data




class UserSerializer(pydantic.BaseModel):
    username: str
    password: str


class User(web.View):

    async def post(self):
        user_data = await self.request.json()
        user_serialized = UserSerializer(**user_data)
        user_data = user_serialized.dict()
        new_user = await UserModel.create_instance(**user_data)
        return web.json_response(new_user.to_dict())


    async def get(self):
        user_id = self.request.match_info['user_id']
        user = await UserModel.get(int(user_id))
        user_data = user.to_dict()
        return web.json_response(user_data)



async def init_orm(app):
    print('приложение стартовало')

    await db.set_bind(PG_DSN)
    await db.gino.create_all()
    yield
    await db.pop_bind().close()


app.add_routes([web.post('/user', User)])
app.add_routes([web.get('/user/{user_id:\d+}', User)])
app.cleanup_ctx.append(init_orm)

web.run_app(app, port=8080)
