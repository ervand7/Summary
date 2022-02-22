from datetime import datetime

from flask import render_template, request, redirect, jsonify, make_response

from . import app


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


@app.route('/sign-up', methods=['GET', 'POST', ])
def sign_up():
    if request.method == 'POST':
        req = request.form
        username = req['username']
        email = req['email']
        password = req['password']
        print(username, email, password)

        return redirect(request.url)

    return render_template('public/sign_up.j2')


users = {
    "mitsuhiko": {
        "name": "Armin Ronacher",
        "bio": "Creatof of the Flask framework",
        "twitter_handle": "@mitsuhiko"
    },
    "gvanrossum": {
        "name": "Guido Van Rossum",
        "bio": "Creator of the Python programming language",
        "twitter_handle": "@gvanrossum"
    },
    "elonmusk": {
        "name": "Elon Musk",
        "bio": "technology entrepreneur, investor, and engineer",
        "twitter_handle": "@elonmusk"
    }
}


@app.route('/profile/<username>')
def profile(username):
    user = users.get(username)
    return render_template('public/profile.j2', user=user)


@app.route('/multiple/<foo>/<bar>/<baz>')
def multi(foo, bar, baz):
    return f'foo is {foo}, bar is  {bar}, baz is {baz}'


@app.route('/json', methods=['POST', ])
def json():
    if request.is_json:
        req = request.get_json()
        print(type(req), req, sep='\n')

        response = {
            'message': 'json received',
            'name': req.get('name')
        }

        result = make_response(jsonify(response), 200)

        return result
    else:
        result = make_response(jsonify({'message': 'No JSON received'}), 400)
        return result


@app.route('/guestbook')
def guestbook():
    return render_template('public/guestbook.j2')


@app.route('/guestbook/create-entry', methods=['POST', ])
def create_entry():
    req = request.get_json()
    print(req)

    resp = make_response(jsonify(req), 200)
    return resp


@app.route("/query")
def query():

    if request.args:

        # We have our query string nicely serialized as a Python dictionary
        args = request.args

        # We'll create a string to display the parameters & values
        serialized = ", ".join(f"{k}: {v}" for k, v in request.args.items())

        # Display the query string to the client in a different format
        return f"(Query) {serialized}", 200

    else:

        return "No query string received", 200
