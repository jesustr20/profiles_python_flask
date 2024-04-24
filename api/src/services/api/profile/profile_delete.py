from src.model import db
from src.model.model_profile import ProfileModel
from src.schemas.schema_profile import profile_schema
from src.services.errors.error_handling import handle_error

class ProfileDeleteService:
    @staticmethod
    def delete_profile_by_id(id):
        try:
            profile = db.session.query(ProfileModel).filter(ProfileModel.id == id).first()
            if profile:
                db.session.delete(profile)
                db.session.commit()
                return profile_schema.dump(profile)
            else:
                return handle_error(f"Profile with id {id} not found", 404)
        
        except ValueError as ve:
            return handle_error(str(ve), 404)
        except Exception as e:
            return handle_error(f"Internal Server Error: {e}", 500)