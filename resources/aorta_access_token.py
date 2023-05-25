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
        actor_did = "yyy"
        bsn = "xxx"

        receiver_app_id = 1
        sender_app_id = 2

        # OUT: aorta access token
        # 1. check if NutsAuthzCredential is present
        # skip for now
        authzcred_list = Nuts_vcr_client.getAuthzCredentials(actor_did, bsn)

        # 2. then create aorta_access_token using aorta_authorization_client
        
        try:
            endpoint = f"{current_app.config['BASE_URL_LSP']}/token"
            data = request.data
            headers = request.headers
            cert = ('LSP110.csc-lsp.nl.pem', 'LSP110.csc-lsp.nl.key.unencrypted')

            response = requests.post(endpoint, data=data, headers=headers, verify=False, cert=cert)
            response.raise_for_status()
            response_json = response.json()
            access_token = response_json["access_token"]
          
        except Exception as e:
            print("error getting access token", e)
            return {'access token not found': sender_app_id}, 400

        return {    "access_token": access_token
                }, 200