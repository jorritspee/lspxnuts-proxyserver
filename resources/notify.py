from flask import jsonify, request, current_app
from flask_restful import Resource
import base64, urllib.parse, requests
from aorta.aorta_notification_transformer import Aorta_notification_transformer
from aorta.aorta_resource_client import Aorta_resource_client

class Notify(Resource):
  
    # corresponds to the GET request.
    # this function is called whenever there
    # is a GET request for this resource
    def get(self):
  
        return {'invalid method': 'GET', 'please use': 'POST'}, 405
    
    """2.15 Notify - create Task"""
    # Corresponds to incoming POST request
    def post(self):         
        try:
            data = request.get_json()
        except:
            return { "error": "invalid json in request body" }, 400
        try:
            task_aof = Aorta_notification_transformer.transform_notification(data)
        except:
            return { "error": "transformation of json failed" }, 400
        
        try:
            bearer = request.authorization
            access_token = bearer.split()[1]  # YourTokenHere
        except:
            return { "error": "no bearer token present" }, 400
        
        try:
            response = Aorta_resource_client.call_lsp_create_task(task_aof, access_token)
            return response.json(), response.status_code
        except:
            return { "error": "forwarding of notification request failed" }, 500
    
    