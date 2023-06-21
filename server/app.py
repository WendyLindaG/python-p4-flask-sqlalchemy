#!/usr/bin/env python3

from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from flask_migrate import Migrate

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///app.db'

db = SQLAlchemy()
db.init_app(app)

migrate = Migrate(app, db)

# Import the models module after initializing SQLAlchemy
from models import *

if __name__ == '__main__':
    app.run(port=5555)
