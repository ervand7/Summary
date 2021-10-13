from flask import request, jsonify
from flask.views import MethodView

from app import app
from validator import validate
from models import User
from schema import schema


class UserView(MethodView):

    def get(self, user_id):
        user = User.by_id(user_id)
        return jsonify(user.to_dict())

    @validate('json', schema)
    def post(self):
        user = User(**request.json)
        user.set_password(request.json['password'])
        user.add()
        return jsonify(user.to_dict())


@app.route('/health/', methods=['GET', ])
def health():
    if request.method == 'GET':
        return jsonify({'status': 'OK'})

    return {'status': 'OK'}


app.add_url_rule('/users/<int:user_id>', view_func=UserView.as_view('users_get'), methods=['GET', ])
app.add_url_rule('/users/', view_func=UserView.as_view('users_create'), methods=['POST', ])
