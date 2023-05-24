from flask import jsonify, request, current_app
from flask_restful import Resource

class Hello(Resource):
  
    # corresponds to the GET request.
    # this function is called whenever there
    # is a GET request for this resource
    def get(self):
        return {
                "hello": "world",
                "you": "are doing great! keep up the good work",
                "config": {
                    "base url nuts node": current_app.config["BASE_URL_NUTS_NODE"],
                    "base url lsp": current_app.config["BASE_URL_LSP"],
                    "lsp application id": current_app.config["LSP_APPLICATION_ID"],
                    "filename transation token": current_app.config["FILENAME_TRANSACTION_TOKEN"]
                },
                "resources": ["/", "/request-access-token", "/notify"]
            }
        #return {'task': 'Hello world'}

        #return make_response(jsonify({'message': 'hello world'}), 200)
  
    # Corresponds to POST request
    def post(self):

        data = request.get_json()     # status code
        #return jsonify(1,2,3), 201
        return data, 201
        #return jsonify(data), 201
        #return jsonify({'data': data}), 201