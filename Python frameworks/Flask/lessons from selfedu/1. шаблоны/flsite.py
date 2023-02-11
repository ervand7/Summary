from flask import Flask, render_template

app = Flask(__name__)  # создаем экземпляр класса Flask

menu = ['Установка', 'Первое приложение', 'Обратная связь']


@app.route('/index')
@app.route('/')
def index():
    return render_template('index.html', title='Про Flask', menu=menu)


@app.route('/about')
def about():
    return render_template('about.html', title='О сайте', menu=menu)


if __name__ == '__main__':
    app.run(debug=True)
