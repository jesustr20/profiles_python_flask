from flask import Flask
from flask_migrate import Migrate
from .api.api_users import api_bp
from .api.authorization import auth_bp
from .api.api_profile import api_pf_bp
from .schemas.schema import ma
from .config.swagger import Swagger
from .model import db, create_db
from .config.config import Config

migrate = Migrate()

def create_app():
    app = Flask(__name__)
    Config.init_app(app)
    Swagger.init_app(app)    
    db.init_app(app)
    ma.init_app(app)
    from src.migrates import UserModel, ProfileModel
    migrate.init_app(app, db)
    app.register_blueprint(api_bp, url_prefix='/api')
    app.register_blueprint(auth_bp, url_prefix='/auth')
    app.register_blueprint(api_pf_bp, url_prefix='/api')

    with app.app_context():
        create_db(app.config["SQLALCHEMY_DATABASE_URI"])
        db.create_all()        

    return app