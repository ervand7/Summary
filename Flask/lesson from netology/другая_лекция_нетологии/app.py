import flask
import hashlib
from flask import request
from flask_sqlalchemy import SQLAlchemy
from flask.views import MethodView
from sqlalchemy.exc import IntegrityError

app = flask.Flask('app')
DSN = 'postgresql://my_admin:1234@127.0.0.1:5432/flask_test'

app.config.from_mapping(SQLALCHEMY_DATABASE_URI=DSN)
db = SQLAlchemy(app)


class User(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String(64), index=True, unique=True)
    password = db.Column(db.String(128))
    email = db.Column(db.String(128), index=True, unique=True)


class UserView(MethodView):
    def get(self, user_id):
        user = User.query.get(user_id)
        if user is None:
            raise NotFound
        return flask.jsonify({
            'user': user.id,
            'name': user.username,
            'email': user.email,
            'password': user.password
        })

    def post(self):
        user_data = request.json
        password = user_data['password']
        password_hash = hashlib.md5(password.encode()).hexdigest()
        user_data['password'] = password_hash
        try:
            user = User(**user_data)
            db.session.add(user)
            db.session.commit()
            return flask.jsonify({'id': user.id})
        except IntegrityError:
            raise BadRequest


class NotFound(Exception):
    message = 'Not Found'
    status_code = 404


class BadRequest(Exception):
    message = 'Already exists'
    status_code = 400


@app.errorhandler(BadRequest)
@app.errorhandler(NotFound)
def error_handler(error):
    response = flask.jsonify({
        'error': error.message
    })
    response.status_code = error.status_code
    return response


app.add_url_rule('/users/<int:user_id>', view_func=UserView.as_view('user_get'), methods=['GET'])
app.add_url_rule('/users/', view_func=UserView.as_view('user_post'), methods=['POST'])


@app.route('/health', methods=['GET'])
def health_check():
    return flask.jsonify({
        'status': 'OK'
    })


app.run(port=8000)
