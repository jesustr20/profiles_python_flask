from flask import jsonify
from sqlalchemy.exc import InvalidRequestError
from src.services.errors.error_handling import handle_error
from src.model import db
from src.model.model_user import UserModel
from src.schemas.schema_user import user_schema

class UsersIdGetService:
    @staticmethod
    def get_user_by_id(id):
        try:
            
            user = db.session.query(UserModel).filter(UserModel.id == id).first()
            
            if user:
                user_data = user_schema.dump(user)
                return jsonify(user_data)            
            else:
                return handle_error(f"User with id {id} not found", 404)            
        except InvalidRequestError as e:
            return handle_error(f"Invalid request {e}", 400, f"User with id {id} not found")
        except Exception as e:
            return handle_error(f"Internal Server Error: {e}", 500)
