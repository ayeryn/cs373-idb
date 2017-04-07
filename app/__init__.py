from flask import Flask

app = Flask(__name__)
app.config.from_object('config')

from app import models, views
from models import db

db.app = app
db.init_app(app)


