from flask import jsonify, request, current_app
from flask_restful import Resource
from nuts.nuts_vcr_client import Nuts_vcr_client
import requests

class Admin_Issue_UraCredential(Resource):

    def get(self):
        return {"you": "did a get"}

    def post(self):
        try:
            data = request.get_json()
            subject_did = data['subject']
            subject_ura = data['ura']
        except Exception as e:
            return {
                "invalid request body, use":
                {
                    "subject": "<did:nuts of subject>",
                    "ura": "urn:oid: 2.16.528.1.1007.3.3.<ura of subject>"
                }
            }, 406

        endpoint = current_app.config["BASE_URL_NUTS_NODE"] + "/internal/vcr/v2/issuer/vc"
        requestObj = {
                        "@context": "https://nuts.nl/credentials/v1",
                        "type": "VzvzUraCredential",
                        "issuer": current_app.config['VENDOR_DID'],
                        "credentialSubject": {
                            "id": subject_did,
                            "nuts:ura": "urn:oid:2.16.528.1.1007.3.3." + subject_ura
                        },
                        "visibility": "public",
                        "publishToNetwork": True
                    }

        response = requests.post(endpoint, json=requestObj)
        response.raise_for_status()

        return response.json(), response.status_code
