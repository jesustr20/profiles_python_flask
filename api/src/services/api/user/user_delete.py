from src.model import db
from src.model.model_user import UserModel
from src.schemas.schema_user import user_schema
from src.services.errors.error_handling import handle_error

class UserDeleteService:
    @staticmethod
    def delete_user_by_id(id):
        try:
            user = db.session.query(UserModel).filter(UserModel.id == id).first()
            if user:
                db.session.delete(user)
                db.session.commit()
                return user_schema.dump(user)
            else:
                return handle_error(f"User with id {id} not found", 404)
        except ValueError as ve:
            return handle_error(str(ve), 404)
        except Exception as e:
            return handle_error(f"Internal Server Error: {e}", 500)