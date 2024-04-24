from decouple import config
import datetime
import jwt
import pytz

class Security():
    secret = config('JWT_KEY')
    tz = pytz.timezone('America/Lima')

    @classmethod
    def generate_token(cls, authenticated_user):
        payload = {
            'iat': datetime.datetime.now(tz=cls.tz),
            'exp': datetime.datetime.now(tz=cls.tz) + datetime.timedelta(minutes=10),
            'username': authenticated_user.username,
            'email': authenticated_user.email,
        }
        
        return jwt.encode(payload, cls.secret, algorithm="HS256")
    
    @classmethod
    def verify_token(cls, headers):
        if 'Authorization' in headers:
            authorization = headers['Authorization']
            encoded_token = authorization.split(' ')[1]
            try:
                jwt.decode(encoded_token, cls.secret, algorithms=["HS256"])
                return True
            except (jwt.ExpiredSignatureError, jwt.InvalidTokenError):
                return False
        
        return False