from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from flask_login import LoginManager
from sqlalchemy import inspect


db = SQLAlchemy()

def create_app():
    app = Flask(__name__, instance_relative_config=False)
    app.config['SECRET_KEY'] = 'dev'
    app.config['SQLALCHEMY_DATABASE_URI'] = 'mysql+mysqlconnector://root:alpha12345@localhost/gotripv2'
    db.init_app(app)

    from .views import views
    from .auth import auth

    app.register_blueprint(views, url_prefix='/')
    app.register_blueprint(auth, url_prefix='/')

    from .module import User

    login_manager = LoginManager()
    login_manager.login_view = 'auth.login'
    login_manager.init_app(app)

    @login_manager.user_loader
    def load_user(id):
        return User.query.get(int(id))
    
    @login_manager.unauthorized_handler
    def unauthorized():
        return 'You must be logged in to access this page.', 403
    

    with app.app_context():
        inspector = inspect(db.engine)
        if not inspector.get_table_names():  # checks if any tables exist in the database
            db.create_all()
            print('Created Database!')

    return app
