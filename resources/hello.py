from flask import jsonify, request, current_app
from flask_restful import Resource

class Hello(Resource):
  
    # corresponds to the GET request.
    # this function is called whenever there
    # is a GET request for this resource
    def get(self):
        return {'task': current_app.config["BASE_URL_NUTS_NODE"]}
        #return {'task': 'Hello world'}

        #return make_response(jsonify({'message': 'hello world'}), 200)
  
    # Corresponds to POST request
    def post(self):

        data = request.get_json()     # status code
        #return jsonify(1,2,3), 201
        return data, 201
        #return jsonify(data), 201
        #return jsonify({'data': data}), 201