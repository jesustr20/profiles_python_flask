from flask import jsonify
from src.utils.security import Security
from src.services.errors.error_handling import handle_error

class AuthLogoutService:
    @staticmethod
    def logout(response):
        try:
            response = jsonify({"message": "Logout successful!"})
            return Security.logout(response), 200
        except Exception as e:
            return handle_error(f"Invalid request: {e}", 400)
            