from flask import Blueprint, request, jsonify
from src.services.errors.error_handling import handle_error
from src.schemas.schema_user import users_schema
from src.services.decorators.secure_required_decorator import TokenRequired
from src.services.decorators.errors import ValidateJSON
from src.services.api.user.user_post import UserPostService
from src.services.api.user.users_get import UsersGetService
from src.services.api.user.users_by_id_get import UsersIdGetService
from src.services.api.user.user_update import UserUpdateService
from src.services.api.user.user_delete import UserDeleteService

api_bp = Blueprint('api_users', __name__)

#Create a new user
@api_bp.route('/register', methods=['POST'])
@ValidateJSON()
def create_user():
    user_data = request.json
    return UserPostService.create_user(user_data)
    
#Get all users and filter by age with query parameter asc and desc and
@api_bp.route('/users', methods=['GET'])
@TokenRequired
def get_users():
    try:            
        users_data = UsersGetService.get_users(request)        
        users = users_schema.dump(users_data)
        return jsonify(data=users)
    except Exception as e:
        return handle_error(f"Invalid request {e}", 400)

#Get user by id
@api_bp.route('/users/<int:id>', methods=['GET'])
@TokenRequired
def get_user_by_id(id):
    return UsersIdGetService.get_user_by_id(id)

#Update user by id
@api_bp.route('/users/<int:id>', methods=['PATCH'])
@TokenRequired
@ValidateJSON()
def update_user_by_id(id):
    return UserUpdateService.update_user_by_id(id, request.json)

#Delete user by id
@api_bp.route('/users/<int:id>', methods=['DELETE'])
@TokenRequired
def delete_user_by_id(id):
    return UserDeleteService.delete_user_by_id(id)