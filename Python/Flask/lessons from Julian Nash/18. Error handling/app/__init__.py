from flask import Flask

app = Flask(__name__)
if app.config['ENV'] == 'production':
    app.config.from_object('configuration.ProductionConfig')
elif app.config['ENV'] == 'testing':
    app.config.from_object('configuration.TestingConfig')
else:
    app.config.from_object('configuration.DevelopmentConfig')

from . import views
from . import admin_views
from . import error_handler
