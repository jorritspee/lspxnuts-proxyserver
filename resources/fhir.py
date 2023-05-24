from flask import jsonify, request, current_app
from flask_restful import Resource

class Fhir(Resource):
  
    # corresponds to the GET request.
    # this function is called whenever there
    # is a GET request for this resource
    def get(self):
        return {"you": "did a get"}
    
    # Corresponds to POST request
    def post(self):
        return { "post not supported": "use GET"}, 405