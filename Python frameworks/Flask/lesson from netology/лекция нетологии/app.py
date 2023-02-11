# pip install flask
from flask import Flask, jsonify, request

from db import get_password, get_hash
from scheme import POST
from validation import validate

app = Flask('my_app')  # my_app - our application name


@app.route('/status', methods=['GET'])
def is_alive():
    """
    Функция для отправки простых GET-запросов.
    """
    return jsonify({'message': 'server is alive'})


@app.route('/test_post/<int:variable>', methods=['POST'])
@validate(POST)
def my_post(variable):
    """
    Тут попробуем использовать валидацию через json-схему.
    """
    return jsonify({
        'headers': dict(request.headers),
        'what_is_in_request': dir(request),
        'data': request.json,
        'variable': variable
    })


@app.route('/check-password', methods=['POST'])
def check_password_through_post():
    """
    Проэмулируем работу с бд.
    """
    login = request.json['login']
    password = request.json['password']
    passw_from_db_hash = get_password(login)
    authorized = (get_hash(password) == passw_from_db_hash)
    response = jsonify({
        'is_authorized': authorized
    })
    response.status_code = 200 if authorized else 401
    return response


@app.route('/check-password2', methods=['GET'])
def check_password_through_get():
    """
    Здесь для наглядности провалидируем ситуацию, когда передача данных
    у клиента будет идти не серез params, а чере урл.
    """
    login = request.args.get('login')
    password = request.args.get('password')
    dp_password = get_password(login)
    authorized = (get_hash(password) == dp_password)
    response = jsonify({
        'is_authorized': authorized
    })
    response.status_code = 200 if authorized else 401
    return response


app.run(port='5051')
