from flask import Flask, render_template, make_response, g, request, flash, abort, url_for, redirect

app = Flask(__name__)


@app.route('/')
def index():
    content = 'Hello'
    res = make_response(content)
    # text/plan делает так, что мы получим чистый html
    res.headers['Content-Type'] = 'text/plan'
    res.headers['Server'] = 'ervand'
    print(f'res {res}')
    print(res.headers)
    return content


@app.route('/image')
def image():
    img = None
    with app.open_resource(app.root_path + "/static/images/ava.png", mode="rb") as f:
        img = f.read()
    if not img:
        return "None image"

    res = make_response(img)
    # image/png делает так, что мы получим картинку
    res.headers['Content-Type'] = 'image/png'
    res.headers['Server'] = 'ervand'
    return res


@app.route('/500')
def index_500():
    content = 'Hello'
    res = make_response(content, 500)
    res.headers['Content-Type'] = 'text/plan'
    res.headers['Server'] = 'ervand'
    print(f'res {res}')
    print(res.headers)
    return content


@app.route('/smth')
def smth():
    """Пример того, как мы кортежем можем передать тело запроса, статус и заголовки."""
    return "<h1>Main Page</h1>", 200, {'Content-Type': 'text/plan'}


@app.route('/my_redirect')
def my_redirect():
    """Пример редиректа."""
    return redirect(url_for('index'), 301)


# функции-хуки:

@app.errorhandler(404)
def pageNot(error):
    """
    Прописав эту функцию с этим декоратором теперь при вводе любого
    несуществующего эндпоинта мы получим 404 и предупреждение."""
    return 'Страница не найдена!', 404


@app.before_first_request
def before_first_request():
    print('before_first_request() called')


@app.before_request
def before_request():
    print('before_request() called')


@app.after_request
def after_request(response):
    print('after_request() called')
    return response


@app.teardown_request
def teardown_request(response):
    print('teardown_request() called')
    return response


if __name__ == '__main__':
    app.run(debug=True)
