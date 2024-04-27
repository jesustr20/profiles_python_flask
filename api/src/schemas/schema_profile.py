from marshmallow.fields import Enum
from marshmallow import fields
from src.schemas.schema import ma
from src.model.model_profile import ProfileModel
from src.entities.gender_enum import Gender

class ProfileSchema(ma.SQLAlchemyAutoSchema):
    class Meta:
        model = ProfileModel
        load_instance = True
        fields = ('id','nickname', 'fname', 'lname', 'document', 'gender','user_id')
    
    gender = Enum(Gender, by_value=True, required=False)
    user_id = fields.Inferred()

profile_schema = ProfileSchema()
profiles_schema = ProfileSchema(many=True)