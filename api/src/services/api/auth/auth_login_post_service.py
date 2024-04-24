from flask import jsonify
from flask_bcrypt import Bcrypt
from src.model.model_user import UserModel
from src.utils.security import Security

bcrypt = Bcrypt()

class AuthLoginService:
    @staticmethod
    def login(user_data):
        try:
            username = user_data.get('username')
            password = user_data.get('password')

            user = UserModel.query.filter_by(username=username).first()
            
            if user and bcrypt.check_password_hash(user.password, password):
                encode_token = Security.generate_token(user)
                return jsonify({"success":True,"token":encode_token ,"message":"Login successfull!"}), 200
            else:
                return jsonify({"Error:":"Invalid username or password"}), 401
        except Exception as e:
            return jsonify({"Error":f"Invalid request {e}"}), 400