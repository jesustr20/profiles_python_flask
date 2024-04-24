from functools import wraps
from flask import jsonify, request
from src.services.errors.error_handling import handle_error

class ValidateJSON:
    def __init__(self, message="Did not attempt to load JSON data because the request Content-Type was not 'application/json'."):
        self.message = message

    def __call__(self, f):
        @wraps(f)
        def decorated_function(*args, **kwargs):
            if request.headers.get('Content-Type') == 'application/json':
                return f(*args, **kwargs)
            else:
                response = {
                    "message": self.message,
                    "status": 415
                }
                return jsonify(response), 415
        return decorated_function