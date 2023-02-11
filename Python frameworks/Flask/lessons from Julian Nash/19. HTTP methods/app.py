from flask import Flask, make_response, jsonify, request, render_template

app = Flask(__name__)

stock = {
    "fruit": {
        "apple": 30,
        "banana": 45,
        "cherry": 1000
    }
}


@app.route("/get-text")
def get_text():
    return "some text"


# passing args through query string
@app.route("/qs")
def qs():
    if request.args:
        req = request.args
        return " ".join(f"{k}: {v}, " for k, v in req.items())

    return "No query"


@app.route("/stock")
def get_stock():
    res = make_response(jsonify(stock), 200)

    return res


@app.route("/stock/<collection>")
def get_collection(collection):
    """ Returns a collection from stock """

    if collection in stock:
        res = make_response(jsonify(stock[collection]), 200)
        return res

    res = res = make_response(jsonify({"error": "Not found"}), 404)

    return res


@app.route("/stock/<collection>/<member>")
def get_member(collection, member):
    """ Returns the qty of the collection member """

    if collection in stock:
        member = stock[collection].get(member)
        if member:
            res = make_response(jsonify(member), 200)
            return res

        res = make_response(jsonify({"error": "Not found"}), 404)
        return res

    res = res = make_response(jsonify({"error": "Not found"}), 404)
    return res


if __name__ == '__main__':
    app.run()
