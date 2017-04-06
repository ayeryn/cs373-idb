from flask import Flask
from models import db


app = Flask(__name__)
app.config.from_object('config')
db.app = app
db.init_app(app)


from app import models, views
