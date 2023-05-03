import sqlite3
import os
from flask import Flask, render_template, g, request, flash, abort
from FDataBase import FDataBase

# конфигурация
DATABASE = '/tmp/flsite.db'
DEBUG = True
SECRET_KEY = 'DFSF8FW8knjdncsidf9few9'

app = Flask(__name__)
app.config.from_object(__name__)  # этой строчкой мы загружаем конфигурацию (DATABASE, DEBUG, SECRET_KEY)
# из нашего приложения. __name__ указывает на то, откуда мы будем загружать

# переопределим путь к бд
app.config.update(dict(DATABASE=os.path.join(app.root_path, 'flsite.db')))


def set_connection():
    """Функция настройки создания связи с БД"""
    conn = sqlite3.connect(app.config['DATABASE'])
    conn.row_factory = sqlite3.Row  # для того, чтобы записи из бд были представленны не в виде кортежей, а в виде dict
    return conn


def create_db():
    """
    Вспомогательная функция для создания таблиц БД. Работает без web-сервера.
    Эту функцию запускаем в модуле create_database.py
    """
    conn = set_connection()
    with app.open_resource('sq_db.sql', mode='r') as create_script:
        conn.cursor().executescript(create_script.read())
    conn.commit()
    conn.close()


def open_db():
    """Установка соединения с бд, если оно еще не установлено."""
    # g - такая же глобальная переменная, как и request или session
    if not hasattr(g, 'conn_db'):
        g.conn_db = set_connection()
    return g.conn_db


@app.teardown_appcontext
def close_db(error):
    """Закрываем соединение с бд, если оно было установлено."""
    if hasattr(g, 'link_db'):
        g.link_db.close()


@app.route('/')
def index():
    """Установка соединения с бд в момент запроса http."""
    db = open_db()
    dbase = FDataBase(db)  # создаем экземпляр класса FDataBase
    return render_template('index.html', menu=dbase.getMenu(), posts=dbase.getPostsAnonce())


@app.route("/add_post", methods=["POST", "GET"])
def addPost():
    db = open_db()
    dbase = FDataBase(db)

    if request.method == "POST":
        if len(request.form['name']) > 4 and len(request.form['post']) > 10:
            dbase.addPost(request.form['name'], request.form['post'], request.form['url'])
            flash('Статья добавлена успешно', category='success')
        else:
            flash('Ошибка добавления статьи!', category='error')

    return render_template('add_post.html', menu=dbase.getMenu(), title="Добавление статьи")


@app.route("/post/<alias>")
def showPost(alias):
    db = open_db()
    dbase = FDataBase(db)
    title, post = dbase.getPost(alias)
    if not title:
        abort(404)

    return render_template('post.html', menu=dbase.getMenu(), title=title, post=post)


if __name__ == "__main__":
    app.run()
