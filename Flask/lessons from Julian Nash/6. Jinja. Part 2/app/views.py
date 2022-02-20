from . import app
from flask import render_template
from datetime import datetime


@app.template_filter('clean_date')
def clean_date(dt: datetime):
    return dt.strftime('%d %b %Y')


@app.route('/')
def index():
    return render_template('public/index.j2')


@app.route('/jinja')
def jinja():
    my_name = "Julian"
    age = 30
    langs = ["Python", "JavaScript", "Bash", "Ruby", "C", "Rust"]
    friends = {
        "Tony": 43,
        "Cody": 28,
        "Amy": 26,
        "Clarissa": 23,
        "Wendell": 39
    }
    colors = ("Red", "Blue")
    cool = True
    date = datetime.utcnow()
    my_html = '<h1>This is some HTML</h1>'
    suspicious = "<script>alert('YOU GOT HACKED')</script>"

    class GitRemote:
        def __init__(self, name, description, domain):
            self.name = name
            self.description = description
            self.domain = domain

        def pull(self):
            return f"Pulling repo {self.name}"

        def clone(self):
            return f"Cloning into {self.domain}"

    my_remote = GitRemote(
        name="Learning Flask",
        description="Learn the Flask web framework for Python",
        domain="https://github.com/Julian-Nash/learning-flask.git"
    )

    # Functions
    def repeat(x, qty=1):
        return x * qty

    return render_template(
        'public/jinja.j2',
        my_name=my_name, age=age, langs=langs, friends=friends,
        colors=colors, cool=cool, GitRemote=GitRemote, repeat=repeat,
        my_remote=my_remote, date=date, my_html=my_html, suspicious=suspicious
    )


@app.route('/about')
def about():
    return "<h1 style='color: red'>About!!!</h1>"
