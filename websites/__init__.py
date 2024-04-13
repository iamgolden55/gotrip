from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from os import path

db = SQLAlchemy()
DB_NAME = "database.db"
# DB_NAME = "world_hotels

def create_app():
    app = Flask(__name__)
    app.config['SECRET_KEY'] = 'dev'
    app.config['SQLALCHEMY_DATABASE_URI'] = f'sqlite:///{DB_NAME}'
    db.init_app(app)


    from .views import views
    from .auth import auth

    app.register_blueprint(views, url_prefix='/')
    app.register_blueprint(auth, url_prefix='/')

    from .module import City, Hotel, Room, Booking, User
    
    with app.app_context():
        create_database(app)

    return app
# Path: websites/module.py
def create_database(app):
    if not path.exists('websites/' + DB_NAME):
        db.create_all()
        print('Created Database!')