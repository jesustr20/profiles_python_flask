from functools import wraps
from flask import request
from src.services.errors.error_handling import handle_error
from src.utils.security import Security

class TokenRequired:
    def __init__(self,  view_func):
        self.view_func = view_func
        wraps(view_func)(self)
    
    def __call__(self, *args, **kwargs):
        has_access = Security.verify_token(request.headers)
        if not has_access:
            return handle_error("Unauthorized", 401)
        return self.view_func(*args, **kwargs)