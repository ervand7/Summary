import datetime
import hashlib

from flask import Flask, jsonify, request
from flask_jwt_extended import create_access_token, jwt_required, JWTManager, verify_jwt_in_request
from flask_migrate import Migrate
from flask_sqlalchemy import SQLAlchemy
from jsonschema import validate, ValidationError

from schema import AD_CREATE, USER_CREATE

app = Flask(__name__)
jwt = JWTManager(app)
DSN = 'postgresql+psycopg2://my_admin:1234@127.0.0.1:5432/flask_stolen'
app.config['SQLALCHEMY_DATABASE_URI'] = DSN  # os.getenv('DATABASE_URL', '').replace('postgres', 'postgresql+psycopg2')
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
SALT = 'my_salt'
db = SQLAlchemy(app)
migrate = Migrate(app, db)
app.config['JWT_SECRET_KEY'] = 't1NP63m4wnBg6nyHYKfmc2TpCOGI4nss'


class Ad(db.Model):
    __tablename__ = 'ads'
    id = db.Column(db.Integer, primary_key=True)
    title = db.Column(db.String(100), nullable=False)
    description = db.Column(db.Text, nullable=False)
    date = db.Column(db.DateTime, default=datetime.datetime.utcnow)
    author = db.Column(db.Integer, db.ForeignKey('user.id'))

    def __str__(self):
        return '<Ad {}>'.format(self.title)

    def __repr__(self):
        return str(self)

    def to_dict(self):
        return {
            'title': self.title,
            'description': self.description,
            'author': self.author
        }


class User(db.Model):
    __tablename__ = 'user'
    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String(64), index=True, unique=True)
    email = db.Column(db.String(120), index=True, unique=True)
    password = db.Column(db.String(128))
    token = db.Column(db.String(500), unique=True)

    def __str__(self):
        return '<User {}>'.format(self.username)

    def __repr__(self):
        return str(self)

    def set_password(self, raw_password: str):
        raw_password = f'{raw_password}{SALT}'
        self.password = hashlib.md5(raw_password.encode()).hexdigest()

    def check_password(self, raw_password: str):
        raw_password = f'{raw_password}{SALT}'
        self.password = hashlib.md5(raw_password.encode()).hexdigest()
        return self.password

    def to_dict(self):
        return {
            'username': self.username,
            "email": self.email
        }


@app.route('/api/v1/user-create/', methods=['POST'], strict_slashes=False)
def create_user():
    """ Функция создания пользователя """
    user = User(**request.json)
    user.set_password(request.json['password'])
    try:
        validate(user.to_dict(), USER_CREATE)
    except ValidationError as er:
        return dict(exception=str(er)), 400
    db.session.add(user)
    db.session.commit()
    return jsonify({'status': 'CREATED'}), 201


@app.route('/', methods=['GET'], strict_slashes=False)
def home():
    return "Hello world!"


@app.route('/api/v1/auth/login', methods=['POST'], strict_slashes=False)
def login():
    """Функция авторизации пользователя с присвоением токена"""
    user = User(
        username=request.json['username'],
        password=request.json['password'],
        token=None
    )
    authorized = user.check_password(request.json['password'])
    if not authorized:
        return {'error': 'Username or password invalid'}, 401
    expires = datetime.timedelta(days=7)
    access_token = create_access_token(identity=str(user.id), expires_delta=expires)
    user = db.session.query(User).filter_by(username=request.json['username']).first()
    user.token = access_token
    db.session.commit()
    return jsonify({'token': access_token}), 200


@jwt_required
@app.route('/api/v1/user-info/<int:_id>', methods=['GET'], strict_slashes=False)
def user_detail(_id):
    """Функция вывода информации о пользователе."""
    user = User.query.get(_id)
    verify_jwt_in_request()
    token = (dict(request.headers))['Authorization'].split(' ')[1]
    user_info = User.query.filter_by(token=token).first()
    if user_info is None:
        return "Токен не существует - проверьте правильность ввода"
    if user.id == user_info.id:
        return jsonify(user.to_dict())
    else:
        return "Просматривать можно только информацию информацию о себе"


@jwt_required
@app.route('/api/v1/user-info/<int:_id>/del', methods=['GET'], strict_slashes=False)
def user_del(_id):
    """ Функция удаления пользователя """
    user = db.session.query(User).filter_by(id=_id).first()
    if user is None:
        return "Выбранный ID, для удаления, не существует - проверьте правильность ввода", 400
    token = (dict(request.headers))['Authorization'].split(' ')[1]
    user_info = User.query.filter_by(token=token).first()
    if user_info is None:
        return "Токен не существует - проверьте правильность ввода"
    if user.id == user_info.id:
        try:
            verify_jwt_in_request()
            db.session.delete(user)
            db.session.commit()
            return jsonify({'status': 'NO CONTENT'}), 204
        except:
            return "При удалении произошла ошибка"
    else:
        return "Удалить можно только свой аккаунт", 403


@app.route('/api/v1/ad-info/<int:id>', methods=['GET'], strict_slashes=False)
def ad_info(id):
    """ Функция просмотра объявлений по ID """
    ad = Ad.query.get(id)
    if ad is None:
        return "Выбранный ID объявления не существует - проверьте правильность ввода"
    return jsonify(ad.to_dict())


@jwt_required
@app.route('/api/v1/ad-create/', methods=['POST'], strict_slashes=False)
def create_ad():
    """Функция создания объявления"""
    token = (dict(request.headers))['Authorization'].split(' ')[1]
    user_info = User.query.filter_by(token=token).first()
    if user_info is None:
        return "Токен не существует - проверьте правильность ввода"
    title = request.json['title']
    description = request.json['description']
    author = user_info.id
    ad = Ad(title=title, description=description, author=author)
    try:
        verify_jwt_in_request()
        validate(ad.to_dict(), AD_CREATE)
        db.session.add(ad)
        db.session.commit()
        return jsonify({'status': 'CREATED'}), 201
    except:
        return "При добавлении объявления произошла ошибка"


@jwt_required
@app.route('/api/v1/ad-info/<int:id>/update/', methods=['POST'], strict_slashes=False)
def update_ad(id):
    """ Функция обновления объявления """
    ad = db.session.query(Ad).filter_by(id=id).first()
    if ad is None:
        return "Выбранный ID объявления не существует - проверьте правильность ввода"
    token = (dict(request.headers))['Authorization'].split(' ')[1]
    user_info = User.query.filter_by(token=token).first()
    if user_info is None:
        return "Токен не существует - проверьте правильность ввода"
    if ad.author == user_info.id:
        new_title, new_description = request.json['title'], request.json['description']
        ad.title = new_title
        ad.description = new_description
        ad.author = user_info.id
        try:
            data_for_update = Ad(title=new_title, description=new_description, author=user_info.id)
            validate(data_for_update.to_dict(), AD_CREATE)
            db.session.commit()
            return jsonify({'status': 'OK'}), 200
        except:
            return "При редактировании статьи произошла ошибка"
    else:
        return "Редактировать можно только свои объявления"


@jwt_required
@app.route('/api/v1/ad-info/<int:id>/del', methods=['GET'], strict_slashes=False)
def ad_del(id):
    """ Функция удаления объявления """
    ad = db.session.query(Ad).filter_by(id=id).first()
    if ad is None:
        return "Выбранный ID объявления не существует - проверьте правильность ввода"
    token = (dict(request.headers))['Authorization'].split(' ')[1]
    user_info = User.query.filter_by(token=token).first()
    if user_info is None:
        return "Токен не существует - проверьте правильность ввода"
    if ad.author == user_info.id:
        try:
            db.session.delete(ad)
            db.session.commit()
            return jsonify({'status': 'NO CONTENT'}), 204
        except:
            return "При удалении статьи произошла ошибка"
    else:
        return "Удалять можно только свои объявления"


db.create_all()
