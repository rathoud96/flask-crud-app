# app/__init__.py

# third-party imports
from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from flask_script import Manager
from flask_migrate import Migrate, MigrateCommand



# local imports
from config import app_config
from flask import request, jsonify

# db variable initialization
db = SQLAlchemy()


def create_app(config_name):
    app = Flask(__name__, instance_relative_config=True)
    app.config.from_object(app_config[config_name])
    app.config.from_pyfile('config.py')
    db.init_app(app)

    migrate = Migrate(app, db)

    from app import models
    from .models import User
    import json

    # temporary route
    @app.route('/')
    def hello_world():
        return 'Hello, World!'
    
    @app.route('/user', methods=['GET', 'POST'])
    def create():
        if request.method == 'POST':
            data = request.json
            user = User(email=data['email'],
            username=data['username'])

            db.session.add(user)
            db.session.commit()
            return "user created"
        else:
            users = User.query.all()
            users_list = []
            for user in users:
                users_list.append({'username': user.username, 'email': user.email})
            return jsonify(users_list)

    return app