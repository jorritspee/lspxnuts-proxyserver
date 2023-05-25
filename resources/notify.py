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
            access_token = request.authorization.token
        except:
            return { "error": "no bearer token present" }, 400

        try:
            response = Aorta_resource_client.call_lsp_create_task(task_aof, access_token)
            print("-----BEGIN-------Notify body: -------------")
            content_type = response.headers.get("content-type", "no content type available")
            print("Content-Type: " + content_type)
            if "text" in content_type:
                print(response.text)
                if "Ongeldig bericht of handtekening" in response.text:
                    # hacked response
                    return "", response.status_code
                return response.text, response.status_code
            elif "json" in content_type:
                print(response.json())
            print("-----END-------Notify body: -------------")
            return response.json(), response.status_code
        except Exception as e:
            print("-----BEGIN-------Notify expcetion: -------------")
            print(e)
            print("-----END-------Notify expcetion: -------------")

            return { "error": "forwarding of notification request failed" }, 500

