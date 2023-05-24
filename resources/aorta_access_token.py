from flask import jsonify, request, current_app
from flask_restful import Resource
import base64, urllib.parse, requests
from aorta.aorta_authorization_client import Aorta_authorization_client
from aorta.aorta_addressing_client import Aorta_addressing_client
from nuts.nuts_vcr_client import Nuts_vcr_client
import jwt

class Aorta_access_token(Resource):
    
    def get(self):
        return {'invalid method': 'GET', 'please use': 'POST'}, 405
    
    def post(self):
        # IN: aorta access troken request
        # OUT: aorta access token
        return {"you": "smell"},200