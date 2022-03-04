from . import app
from flask import render_template, request


@app.errorhandler(404)
def not_found(error):
    app.logger.error(request.url)
    return render_template('public/404.j2')
