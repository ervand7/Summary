from flask_sqlalchemy import SQLAlchemy
from flask import Flask, render_template, request, redirect, url_for
from datetime import datetime

from werkzeug.security import generate_password_hash

app = Flask(__name__)
DSN = 'postgresql://my_admin:1234@127.0.0.1:5432/flask_test'
# определение этой константы связывает SQLAlchemy с той или иной субд
app.config['SQLALCHEMY_DATABASE_URI'] = DSN
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

db = SQLAlchemy(app)


class Users(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    email = db.Column(db.String(50), unique=True)
    psw = db.Column(db.String(500), nullable=True)
    date = db.Column(db.DateTime, default=datetime.utcnow())

    def __repr__(self):
        return f'<users {self.id}>'


class Profiles(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(50), unique=True)
    old = db.Column(db.Integer)
    city = db.Column(db.String(100))

    user_id = db.Column(db.Integer, db.ForeignKey('users.id'))

    def __repr__(self):
        return f'<profiles {self.id}>'


@app.route("/")
def index():
    info = []
    try:
        info = Users.query.all()
    except:
        print("Ошибка чтения из БД")

    return render_template("index2.html", title="Главная", list=info)


@app.route("/register", methods=("POST", "GET"))
def register():
    if request.method == "POST":
        # здесь должна быть проверка корректности введенных данных
        try:
            hash = generate_password_hash(request.form['psw'])
            u = Users(email=request.form['email'], psw=hash)
            db.session.add(u)
            db.session.flush()

            p = Profiles(name=request.form['name'], old=request.form['old'],
                         city=request.form['city'], user_id=u.id)
            db.session.add(p)
            db.session.commit()
        except:
            db.session.rollback()
            print("Ошибка добавления в БД")

        return redirect(url_for('index'))

    return render_template("register.html", title="Регистрация")


if __name__ == '__main__':
    app.run(debug=True)
