from flask import Flask, render_template, request, flash, url_for

app = Flask(__name__)
app.config['SECRET_KEY'] = 'SDFSDFsr4t5u7u7tj'

menu = [
    {'name': 'Установка', 'url': 'install-flask'},
    {'name': 'Первое приложение', 'url': 'first-app'},
    {'name': 'Обратная связь', 'url': 'contact'}
]


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


@app.route('/contact', methods=['POST', 'GET'])
def contact():
    if request.method == 'POST':
        # используем функцию flash. Далее, уже в шаблоне contact.html будем получать сообщения
        # от этого flash через get_flashed_messages
        if len(request.form['username']) > 2:
            # category - это для связи с .flash.success и .flash.error из styles.css
            flash('Сообщение отправлено', category='success')
        else:
            flash('Ошибка отправки', category='error')

    return render_template('contact.html', title='Обратная связь', menu=menu)


if __name__ == '__main__':
    app.run(debug=True)
