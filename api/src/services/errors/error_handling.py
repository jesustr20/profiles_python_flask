from flask import jsonify
def handle_error(error, status_code, message=None):
    if message:
        response = jsonify({"Error":str(error), "Message":message})
    else:
        response = jsonify({"Error":str(error)})
    response.status_code = status_code
    return response