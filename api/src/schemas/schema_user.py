from marshmallow.fields import Enum, Nested
from marshmallow import fields
from src.schemas.schema import ma
from src.model.model_user import UserModel
from src.entities.persontype_enum import PersonType
from src.schemas.schema_profile import ProfileSchema

class UserSchema(ma.SQLAlchemyAutoSchema):
    
    class Meta:
        model = UserModel
        load_instance = True
        include_relationships = True        
        fields = ('id', 'username', 'age', 'email', 'category', 'profile')
    
    category = Enum(PersonType, by_value=True, required=False)
    profile = fields.Nested(ProfileSchema, many=True)

user_schema = UserSchema()
users_schema = UserSchema(many=True)