from flask_sqlalchemy import SQLAlchemy

db = SQLAlchemy()

def create_db(url_db:str):
    from sqlalchemy import create_engine
    from sqlalchemy_utils import database_exists, create_database

    engine = create_engine(url_db)
    if not database_exists(engine.url):
        create_database(engine.url)
    print(database_exists(engine.url))
    
