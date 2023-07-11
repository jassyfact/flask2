from flask import Flask 
from flask_migrate import Migrate
from flask_sqlalchemy import SQLAlchemy
import config

db = SQLAlchemy()
migrate = Migrate()

def create_app():
    app = Flask(__name__)

    app.config.from_object(config)

    # ORM
    db.init_app(app)
    migrate.init_app(app, db)

    from .views import basic_views
    app.register_blueprint(basic_views.fisa)


    @app.route('/about_me')
    def about_me():
        return f'저는 {__name__} 입니다' 

    @app.route('/hello')
    def hello():
        return f'안녕하세요' 

    @app.route('/bye')
    def bye():
        return f'잘 가세요 ' 
    
    return app