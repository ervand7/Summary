from flask import Flask, render_template, url_for

app = Flask(__name__)  # создаем экземпляр класса Flask

menu = ['Установка', 'Первое приложение', 'Обратная связь']


@app.route('/')
def index():
    print(url_for('index'))
    return render_template('index.html', menu=menu)


@app.route('/about')
def about():
    print(url_for('about'))
    return render_template('about.html', title='О сайте', menu=menu)


@app.route('/profile/<path:username>')  # есть еще фильтры int и float
def profile(username):
    return f'Пользователь: {username}'


# мы можем вызвать url_for вне функции, если искусственно создадим контекст запроса
# Обратите внимание, что сервер не запускается. Всю эту ситуацию можно назвать как тестовый контекст запроса
with app.test_request_context():
    print(url_for('index'))
    print(url_for('about'))
    print(url_for('profile', username='selfedu'))

# if __name__ == '__main__':
#     app.run(debug=True)
