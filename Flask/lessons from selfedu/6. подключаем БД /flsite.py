import sqlite3
import os
from flask import Flask, render_template, g

# конфигурация
DATABASE = '/tmp/flsite.db'
DEBUG = True
SECRET_KEY = 'DFSF8FW8knjdncsidf9few9'

app = Flask(__name__)
app.config.from_object(__name__)  # этой строчкой мы загружаем конфигурацию (DATABASE, DEBUG, SECRET_KEY)
# из нашего приложения. __name__ указывает на то, откуда мы будем загружать

# переопределим путь к бд
app.config.update(dict(DATABASE=os.path.join(app.root_path, 'flsite.db')))


def connect_db():
    """Функция для установления связи с БД"""
    conn = sqlite3.connect(app.config['DATABASE'])
    conn.row_factory = sqlite3.Row  # для того, чтобы записи из бд были представленны не в виде кортежей, а в виде dict
    return conn


def create_db():
    """Вспомогательная функция для создания таблиц БД без web-сервера."""
    db = connect_db()
    with app.open_resource('sq_db.sql', mode='r') as f:
        db.cursor().executescript(f.read())
    db.commit()
    db.close()


def get_db():
    """Установка соединения с бд, если оно еще не установлено."""
    # g - такая же глобальная переменная, как и request или session
    if not hasattr(g, 'link_db'):
        g.link_db = connect_db()
    return g.link_db


@app.route('/')
def index():
    """Установка соединения с бд в момент запроса http."""
    db = get_db()
    return render_template('index.html', menu=[])


@app.teardown_appcontext
def close_db(error):
    """Закрываем соединение с бд, если оно было установлено."""
    if hasattr(g, 'link_db'):
        g.link_db.close()


if __name__ == "__main__":
    app.run(host='127.0.0.1', port=5002)
