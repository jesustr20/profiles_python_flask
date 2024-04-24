from werkzeug.exceptions import (NotFound, BadRequest, 
                                 InternalServerError, 
                                 MethodNotAllowed)

from src import create_app
from src.services.errors.error_handling import handle_error

app = create_app()

@app.errorhandler(NotFound)
def not_found(e):
    return handle_error(str(e), 404)

@app.errorhandler(MethodNotAllowed)
def method_not_allowed(e):
    return handle_error(str(e), 405)

@app.errorhandler(BadRequest)
def bad_request(e):
    return handle_error(str(e), 400)    

@app.errorhandler(InternalServerError)
def internal_server_error(e):
    return handle_error(str(e), 500)


if __name__ == '__main__':
    app.run(host="0.0.0.0", debug=True)