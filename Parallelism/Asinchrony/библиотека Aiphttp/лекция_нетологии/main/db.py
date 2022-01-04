from gino import Gino

DSN = 'postgres://lesson_aiohttp:lesson_aiohttp@localhost:5432/lesson_aiohttp'
db = Gino()


class User(db.Model):
    __tablename__ = 'test_app_users'

    id = db.Column(db.Integer(), primary_key=True)
    email = db.Column(db.String(128), nullable=False)
    password_hash = db.Column(db.String(256), nullable=False)

    # прописываем индекс, чтобы ускорить поиск по БД
    _idx_email = db.Index('test_app_users_email', 'email', unique=True)


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
