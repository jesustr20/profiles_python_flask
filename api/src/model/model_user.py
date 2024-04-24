from src.entities.persontype_enum import PersonType
from src.model import db

class UserModel(db.Model):
    __table_args__ = {'extend_existing': True}
    __tablename__ = 'users'

    id = db.Column(db.Integer, primary_key=True)    
    age = db.Column(db.Integer, nullable=False)
    category = db.Column(db.Enum(PersonType), nullable=False)    
    username = db.Column(db.String(200), nullable=False, unique=True)
    password = db.Column(db.String(200), nullable=False)
    email = db.Column(db.String(200), nullable=False, unique=True)

    def set_category(self):
        self.category = PersonType.MENOR
        if self.age >= 18:
            self.category = PersonType.MAYOR
    
    def update(self, data):
        for key, value in data.items():
            setattr(self, key, value)

    def __repr__(self):
        return f'<User {self.username}>'