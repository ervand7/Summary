from flask import Flask, render_template, make_response, g, request, flash, abort, url_for, redirect

app = Flask(__name__)


@app.route('/')
def index():
    return "<h1>Main Page</h1>"


@app.route('/login')
def login():
    log = ''
    if request.cookies.get('logged'):
        log = request.cookies.get('logged')

    res = make_response(f'<h1>Форма авторизации</h1><p>logged: {log}', 30*24*3600)
    res.set_cookie('logged', 'yes')
    return res


@app.route('/logout')
def logout():
    log = ''
    res = make_response(f'<p>Вы больше не авторизованы!</p>')
    res.set_cookie('logged', '', max_age=0)
    return res


if __name__ == '__main__':
    app.run(debug=True)
