from flask import Flask
import redis
from rq import Queue

app = Flask(__name__)

r = redis.Redis()

q = Queue(connection=r)

from . import views
from . import tasks
