import os

from flask import Flask
from flask_sqlalchemy import SQLAlchemy

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = os.getenv('DATABASE_URL', '')
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
db = SQLAlchemy(app)


class UserModel(db.Model):
    __tablename__ = 'user'

    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String())


@app.route('/')
def home():
    name = os.getenv('ADMINAME', 'Def3')
    result = db.session.execute('SELECT * from user;')
    value = list(result)[0][0]
    return f'Hello {name}! Test value: {value}'


if __name__ == '__main__':
    port = int(os.environ.get("PORT", 5002))
    app.run(debug=True, host='0.0.0.0', port=port)
