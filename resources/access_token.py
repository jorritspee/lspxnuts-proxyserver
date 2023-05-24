from flask import jsonify, request, current_app
from flask_restful import Resource
import base64, urllib.parse, requests
from aorta.aorta_authorization_client import Aorta_authorization_client
from aorta.aorta_addressing_client import Aorta_addressing_client
from nuts.nuts_vcr_client import Nuts_vcr_client
import jwt

class Access_token(Resource):

    # corresponds to the GET request.
    # this function is called whenever there
    # is a GET request for this resource
    def get(self):

        return {'invalid method': 'GET', 'please use': 'POST'}, 405

    """2.4 Request accessToken"""
    # Corresponds to incoming POST request
    def post(self):

        access_token = "geen"
        token_type = "aorta_access_token"
        expires_in = 600

        print(request.data)

        #get parameters from request body
        #see https://nuts-node.readthedocs.io/en/stable/pages/integrating/api.html
        #endpoint: /internal/auth/v1/request-access-token

        grant_type = request.form['grant_type']
        assertion = request.form['assertion']

        print('grant_type: ' + grant_type)
        print('assertion: ' + assertion)

        if grant_type != "urn:ietf:params:oauth:grant-type:jwt-bearer":
            return {'invalid grant_type': grant_type}, 400

        decoded = jwt.decode(assertion, verify=False, algorithms=['ES256'], options={"verify_signature": False})
        print(decoded)

        issuer = decoded['iss']
        subject = decoded['sub']

        issuerURA = Nuts_vcr_client.getURA(issuer)
        if not issuerURA:
            return {'issuer URA not found': issuer}, 400

        subjectURA = Nuts_vcr_client.getURA(subject)
        if not subjectURA:
            return {'subject URA not found': subject}, 400

        print('issuerURA: ' + issuerURA)
        print('subjectURA: ' + subjectURA)

        recieverRoutingInfo = Aorta_addressing_client.call_lsp_get_routing_info(issuerURA)
        if not recieverRoutingInfo:
            return {'routing info not found': issuerURA}, 400

        print(recieverRoutingInfo)


        return 200

        # print('authorizer: ' + did_authorizer)

        #for notification request
        did_receiver = did_authorizer #'did:nuts:EwVMYK2ugaMvRHUbGFBhuyF423JuNQbtpes35eHhkQic' # TODO
        did_sender = did_requester #'did:nuts:EwVMYK2ugaMvRHUbGFBhuyF423JuNQbtpes35eHhkQic' # TODO

        try:
            ura_destination = Nuts_vcr_client.getURA(did_authorizer)
        except:
            ura_destination = "90001235"

        #appid = current_app.config["LSP_APPLICATION_ID"] #is dit het appid van de sender of van van de receiver of van de nuts-proxy?

        access_token = Aorta_authorization_client.call_lsp_token_exchange_request()

        return {    "access_token": access_token,
                    "token_type": token_type,
                    "expires_in": expires_in
                }, 200




#def request_access_token(request_handler):
    #"""2.4 Request accessToken"""
    #result=introspect_access_token(request_handler)
    #if not result:
    #    return
    #content_length = int(request_handler.headers['Content-Length'])
    #post_data_bytes = request_handler.rfile.read(content_length)
    #post_data = post_data_bytes.decode('utf-8')
    #post_data_json = json.loads(post_data)
    #print('authorizer: ' + post_data_json['authorizer'])
    #did_receiver = 'did:nuts:EwVMYK2ugaMvRHUbGFBhuyF423JuNQbtpes35eHhkQic' # TODO
    #did_sender = 'did:nuts:EwVMYK2ugaMvRHUbGFBhuyF423JuNQbtpes35eHhkQic' # TODO
    #call_node_search_receiver(did_receiver)
    #call_lsp_get_routing_info()
    #call_node_search_sender(did_sender)
    # access_token=call_lsp_token_exchange_request()
    # responseCode = 200
    # responseObj = { "access_token": f"{access_token}" } # TODO
    # request_handler.send_response(responseCode)
    # request_handler.send_header('Content-Type', 'application/json')
    # request_handler.end_headers()
    # request_handler.wfile.write(json.dumps(responseObj).encode('utf-8'))

