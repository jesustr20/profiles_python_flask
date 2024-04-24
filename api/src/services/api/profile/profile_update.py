from src.model.model_profile import ProfileModel
from src.schemas.schema_profile import profile_schema
from src.services.errors.error_handling import handle_error
from src.model import db

class ProfileIdUpdateService:
    @staticmethod
    def update_profile_by_id(id, profile_data):
        try:
            profile = db.session.query(ProfileModel).filter(ProfileModel.id == id).first()
            if profile:
                profile.update(profile_data)
                db.session.add(profile)
                db.session.commit()
                update_profile_data = profile_schema.dump(profile)
                return update_profile_data
            else:
                raise ValueError(f"Profile with id {id} not found", 404)
        except ValueError as ve:
            return handle_error(str(ve), 404)
        except Exception as e:
            return handle_error(f"Internal Server Error: {e}", 500)