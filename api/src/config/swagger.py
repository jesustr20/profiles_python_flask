from flask import Flask
from flask_swagger_ui import get_swaggerui_blueprint

SWAGGER_URL = '/swagger'
API_URL = '/static/swagger.json'
SWAGGER_BLUEPRINT = get_swaggerui_blueprint(
    SWAGGER_URL,
    API_URL,
    config={
        'app_name': "Todo List API"
    }
)

class Swagger:
    @staticmethod
    def init_app(app: Flask):
        
        app.register_blueprint(SWAGGER_BLUEPRINT, url_prefix=SWAGGER_URL)