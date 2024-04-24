from flask import jsonify
from sqlalchemy.exc import InvalidRequestError
from src.services.errors.error_handling import handle_error
from src.model import db
from src.model.model_profile import ProfileModel
from src.schemas.schema_profile import profiles_schema

class ProfileGetService:
    @staticmethod
    def get_profiles(profiles_data):
        try:
            profiles_data = db.session.query(ProfileModel).all()
            profiles = profiles_schema.dump(profiles_data)
            return jsonify(data=profiles)
        except InvalidRequestError as e:
            return handle_error(f"Invalid request {e}", 400)
        except Exception as e:
            return handle_error(f"Internal Server Error: {e}", 500)
