from flask import Blueprint, request, Response
from src.services.api.auth.auth_login_post_service import AuthLoginService
from src.services.api.auth.auth_logout_post_service import AuthLogoutService
from src.services.errors.error_handling import handle_error
from src.services.decorators.errors import ValidateJSON


auth_bp = Blueprint('auth', __name__)

@auth_bp.route('/login', methods=['POST'])
@ValidateJSON()
def login():
    try:
        user_data = request.json
        return AuthLoginService.login(user_data)
    except Exception as e:
        return handle_error(f"Invalid request: {e}", 400)

@auth_bp.route('/logout', methods=['POST'])
def logout():
    try:
        response = Response()    
        return AuthLogoutService.logout(response)
    except Exception as e:
        return handle_error(f"Invalid request: {e}", 400)
        