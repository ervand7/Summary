import datetime

from flask import Flask
from flask_alchemydumps import AlchemyDumps
from flask_jwt_extended import JWTManager
from flask_migrate import Migrate
from flask_sqlalchemy import SQLAlchemy
from werkzeug.security import generate_password_hash, check_password_hash

app = Flask(__name__)
jwt = JWTManager(app)
DSN = 'postgresql+psycopg2://my_admin:1234@127.0.0.1:5432/flask_stolen'
SALT = 'my_salt'
app.config['SQLALCHEMY_DATABASE_URI'] = DSN  # os.getenv('DATABASE_URL', '').replace('postgres', 'postgresql+psycopg2')
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
app.config['JWT_SECRET_KEY'] = 't1NP63m4wnBg6nyHYKfmc2TpCOGI4nss'
app.url_map.strict_slashes = False
db = SQLAlchemy(app)
migrate = Migrate(app, db)
alchemydumps = AlchemyDumps(app, db)


class Ad(db.Model):
    __tablename__ = 'ads'
    id = db.Column(db.Integer, primary_key=True)
    title = db.Column(db.String(110), nullable=False)
    description = db.Column(db.Text, nullable=False)
    date = db.Column(db.DateTime, default=datetime.datetime.utcnow)
    author = db.Column(db.Integer, db.ForeignKey('user.id'))

    def __str__(self):
        return '<From database: class Ad, title: {}>'.format(self.title)

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
    ads = db.relationship('Ad', backref=db.backref('user'))

    def __str__(self):
        return '<From database: class User, username: {}>'.format(self.username)

    def __repr__(self):
        return str(self)

    def set_password(self, password: str):
        hash_psw = generate_password_hash(f'{password}{SALT}')
        self.password = hash_psw

    def check_password(self, password: str):
        hash_psw = self.password
        return check_password_hash(hash_psw, f'{password}{SALT}')

    def to_dict(self):
        return {
            'username': self.username,
            "email": self.email
        }


if __name__ == '__main__':
    app.run(debug=True, port=5001)
