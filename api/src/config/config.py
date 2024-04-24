from flask import Flask

class Config:
    @staticmethod
    def init_app(app: Flask):
        #app.config["SQLALCHEMY_DATABASE_URI"] = "sqlite:///database.db"
        app.config["SQLALCHEMY_DATABASE_URI"] = "postgresql://postgres:cibertec@localhost/flask_databases"
        app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
        