from src.entities.gender_enum import Gender
from src.model.model_user import UserModel
from src.model import db

class ProfileModel(db.Model):
    __tablename__ = 'profiles'

    id = db.Column(db.Integer, primary_key=True)
    nickname = db.Column(db.String(200), nullable=False)
    fname = db.Column(db.String(200), nullable=False)
    lname = db.Column(db.String(200), nullable=False)
    document = db.Column(db.String(10), nullable=False, unique=True)
    gender = db.Column(db.Enum(Gender), nullable=False)
    user_id = db.Column(db.Integer, db.ForeignKey('users.id'), nullable=False)

    def update(self, data):
        for key, value in data.items():
            if key == 'gender':
                if value not in [gender.value for gender in Gender]:
                    raise ValueError(f"Invalid gender value: {value}")
                value = Gender(value)
            setattr(self, key, value)
            
    def __repr__(self):
        return f'<Profile {self.nickname}>'