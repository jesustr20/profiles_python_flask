from flask_bcrypt import Bcrypt
from src.model.model_user import UserModel
from src.schemas.schema_user import user_schema
from src.services.errors.error_handling import handle_error
from src.model import db

bcrypt = Bcrypt()

class UserUpdateService:
    @staticmethod
    def update_user_by_id(id, user_data):
        try:
            user = db.session.query(UserModel).filter(UserModel.id == id).first()
            if user:
                user.update(user_data)
                hash_password = bcrypt.generate_password_hash(user_data['password']).decode('utf-8')
                user.password = hash_password

                db.session.add(user)
                db.session.commit()
                update_user_data = user_schema.dump(user)
                return update_user_data
            else:
                raise ValueError(f"User with id {id} not found", 404)
        except ValueError as ve:
            return handle_error(str(ve), 404)
        except Exception as e:
            return handle_error(f"Internal Server Error: {e}", 500)