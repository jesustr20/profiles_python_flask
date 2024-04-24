from sqlalchemy.exc import InvalidRequestError
from src.services.errors.error_handling import handle_error
from src.model import db
from src.model.model_user import UserModel

class UsersGetService:
    @staticmethod
    def get_users(request):
        
        age_order = request.args.get('age')
        
        try:
            query = db.session.query(UserModel)

            if age_order == 'asc':
                users_data = query.order_by(UserModel.age.asc()).all()
            elif age_order == 'desc':
                users_data = query.order_by(UserModel.age.desc()).all()
            else:
                users_data = query.all()
        except InvalidRequestError as e:
            return handle_error(f"Invalid request {e}", 400)
        except Exception as e:
            return handle_error(f"Internal Server Error: {e}", 500)

        return users_data