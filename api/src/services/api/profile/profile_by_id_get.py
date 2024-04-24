from flask import jsonify
from sqlalchemy.exc import InvalidRequestError
from src.services.errors.error_handling import handle_error
from src.model import db
from src.model.model_profile import ProfileModel
from src.schemas.schema_profile import profile_schema

class ProfileIdGetService:
    @staticmethod
    def get_profile_by_id(id):
        try:
            profile = db.session.query(ProfileModel).filter(ProfileModel.id == id).first()

            if profile:
                profile_data = profile_schema.dump(profile)
                return jsonify(profile_data)
            else:
                return handle_error(f"Profile with id {id} not found", 404)
        except InvalidRequestError as e:
            return handle_error(f"Invalid request {e}", 400, f"Profile with id {id} not found")
        except Exception as e:
            return handle_error(f"Internal Server Error: {e}", 500)