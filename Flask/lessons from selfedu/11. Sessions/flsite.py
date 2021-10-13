import datetime

from flask import Flask, session, make_response, g, request, flash, abort, url_for, redirect

# import os
# os.urandom(20).hex()
# Out[4]: 'be398d0f9ebd3ff31b38a314f6b905e303560de0'

app = Flask(__name__)
app.config['SECRET_KEY'] = 'be398d0f9ebd3ff31b38a314f6b905e303560de0'
# явно указываем продолжительность нашей сессии (10 дней)
app.permanent_session_lifetime = datetime.timedelta(days=10)


@app.route('/')
def index():
    if 'visits' in session:
        session['visits'] += 1
    else:
        session['visits'] = 1
    return f"<h1>Main Page</h1><p>Число просмотров {session['visits']}"


data = [1, 2, 3, 4]


@app.route('/session')
def session_data():
    session.permanent = True  # с помощью этого параметра сессия будет сохраняться
    # даже если закрыть браузер
    if 'data' not in session:
        session['data'] = data
    else:
        session['data'][1] += 1
        session.modified = True  # иначе список не будет меняться
    return f"<p>session['data']: {session['data']}"


if __name__ == '__main__':
    app.run(debug=True)
