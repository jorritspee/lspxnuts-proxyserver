#from http.server import HTTPServer, BaseHTTPRequestHandler
from flask import Flask
from flask_restful import Api
from resources.hello import Hello
from resources.access_token import Access_token
from resources.notify import Notify
from resources.fhir import Fhir
from resources.admin import Admin_Issue_UraCredential

import base64, json, logging, requests, urllib.parse

# creating the flask app
app = Flask(__name__)
app.config.from_file("config.json", load=json.load)

# creating an API object
api = Api(app)

# adding the defined resources along with their corresponding urls
api.add_resource(Hello, '/')
api.add_resource(Access_token, '/access-token')
api.add_resource(Notify, '/notify', '/notify/Task')
api.add_resource(Fhir, '/fhir')
api.add_resource(Admin_Issue_UraCredential, '/admin/issue/uracredential')

# driver function
if __name__ == '__main__':
    app.run(debug = True, port=8000)

# ---------
# - Proxy -
# ---------

# def request_access_token(request_handler):
#     """2.4 Request accessToken"""
#     result=introspect_access_token(request_handler)
#     if not result:
#         return
#     content_length = int(request_handler.headers['Content-Length'])
#     post_data_bytes = request_handler.rfile.read(content_length)
#     post_data = post_data_bytes.decode('utf-8')
#     post_data_json = json.loads(post_data)
#     print('authorizer: ' + post_data_json['authorizer'])
#     did_receiver = 'did:nuts:EwVMYK2ugaMvRHUbGFBhuyF423JuNQbtpes35eHhkQic' # TODO
#     did_sender = 'did:nuts:EwVMYK2ugaMvRHUbGFBhuyF423JuNQbtpes35eHhkQic' # TODO
#     call_node_search_receiver(did_receiver)
#     call_lsp_get_routing_info()
#     call_node_search_sender(did_sender)
#     access_token=call_lsp_token_exchange_request()
#     responseCode = 200
#     responseObj = { "access_token": f"{access_token}" } # TODO
#     request_handler.send_response(responseCode)
#     request_handler.send_header('Content-Type', 'application/json')
#     request_handler.end_headers()
#     request_handler.wfile.write(json.dumps(responseObj).encode('utf-8'))

# # --------------
# # - RB Nuts In -
# # --------------

# def create_task(request_handler):
#     """2.15 Notify - create Task"""
#     content_length = int(request_handler.headers['Content-Length'])
#     post_data_bytes = request_handler.rfile.read(content_length)
#     post_data = post_data_bytes.decode('utf-8')
#     post_data_json = json.loads(post_data)
#     task_aof=transform_notification(post_data_json)
#     call_lsp_create_task(task_aof)
#     responseCode = 200
#     responseObj = { "hello": "world" } # TODO
#     request_handler.send_response(responseCode)
#     request_handler.send_header('Content-Type', 'application/json')
#     request_handler.end_headers()
#     request_handler.wfile.write(json.dumps(responseObj).encode('utf-8'))

# def transform_notification(task_ta_np_json):
#     """2.16 transform notification"""
#     task_aof = json.dumps({
#       "resourceType": "Task",
#       "id": "nl-vzvz-TaskNotifiedPull-request-example",
#       "meta": {
#         "profile": [
#           "http://vzvz.nl/fhir/StructureDefinition/nl-vzvz-TaskNotifiedPull"
#         ]
#       },
#       "contained": [
#         {
#           "resourceType": "Device",
#           "id": "device1",
#           "meta": {
#             "profile": [
#               "http://vzvz.nl/fhir/StructureDefinition/nl-vzvz-Device"
#             ]
#           },
#           "identifier": [
#             {
#               "system": "http://fhir.nl/fhir/NamingSystem/aorta-app-id",
#               "value": "110"
#             }
#           ],
#           "deviceName": [
#             {
#               "name": "TestApplicatie",
#               "type": "user-friendly-name"
#             }
#           ],
#           "owner": {
#             "identifier": {
#               "system": "http://fhir.nl/fhir/NamingSystem/ura",
#               "value": "90000380"
#             }
#           }
#         }
#       ],
#       "status": "requested",
#       "intent": "proposal",
#       "code": {
#         "coding": [
#           {
#             "system": "http://vzvz.nl/fhir/CodeSystem/aorta-taskcode",
#             "code": "notified_pull"
#           }
#         ]
#       },
#       "for": {
#         "identifier": {
#           "system": "http://fhir.nl/fhir/NamingSystem/bsn",
#           "value": "012345672"
#         }
#       },
#       "requester": {
#         "reference": "#device1",
#         "type": "Device"
#       },
#       "owner": {
#         "identifier": {
#           "system": "http://fhir.nl/fhir/NamingSystem/ura",
#           "value": "90000380"
#         }
#       },
#       "restriction": {
#         "period": {
#           "end": "2023-05-05T12:00:00+02:00"
#         }
#       },
#       "input": [
#         {
#           "type": {
#             "coding": [
#               {
#                 "system": "http://vzvz.nl/fhir/CodeSystem/TaskParameterType",
#                 "code": "consent_token"
#               }
#             ]
#           },
#           "valueString": "did:nuts:6AiKV8hQx5nMaSfLNByaxiBjN3XBEUx4LmiHh2iYwuYe"
#         },
#         {
#           "type": {
#             "coding": [
#               {
#                 "system": "http://vzvz.nl/fhir/CodeSystem/TaskParameterType",
#                 "code": "query_string"
#               }
#             ]
#           },
#           "valueString": "Patient?_include=Patient:general-practitioner"
#         },
#         {
#           "type": {
#             "coding": [
#               {
#                 "system": "http://vzvz.nl/fhir/CodeSystem/TaskParameterType",
#                 "code": "query_string"
#               }
#             ]
#           },
#           "valueString": "Coverage?_include=Coverage:payor:Patient&_include=Coverage:payor:Organization"
#         },
#         {
#           "type": {
#             "coding": [
#               {
#                 "system": "http://vzvz.nl/fhir/CodeSystem/TaskParameterType",
#                 "code": "query_string"
#               }
#             ]
#           },
#           "valueString": "Consent?category=http://snomed.info/sct|11291000146105"
#         },
#         {
#           "type": {
#             "coding": [
#               {
#                 "system": "http://vzvz.nl/fhir/CodeSystem/TaskParameterType",
#                 "code": "query_string"
#               }
#             ]
#           },
#           "valueString": "Consent?category=http://snomed.info/sct|11341000146107"
#         },
#         {
#           "type": {
#             "coding": [
#               {
#                 "system": "http://vzvz.nl/fhir/CodeSystem/TaskParameterType",
#                 "code": "query_string"
#               }
#             ]
#           },
#           "valueString": "Observation/$lastn?category=http://snomed.info/sct|118228005,http://snomed.info/sct|384821006"
#         },
#         {
#           "type": {
#             "coding": [
#               {
#                 "system": "http://vzvz.nl/fhir/CodeSystem/TaskParameterType",
#                 "code": "query_string"
#               }
#             ]
#           },
#           "valueString": "Condition"
#         },
#         {
#           "type": {
#             "coding": [
#               {
#                 "system": "http://vzvz.nl/fhir/CodeSystem/TaskParameterType",
#                 "code": "query_string"
#               }
#             ]
#           },
#           "valueString": "Observation/$lastn?code=http://snomed.info/sct|365508006"
#         },
#         {
#           "type": {
#             "coding": [
#               {
#                 "system": "http://vzvz.nl/fhir/CodeSystem/TaskParameterType",
#                 "code": "query_string"
#               }
#             ]
#           },
#           "valueString": "Observation?code=http://snomed.info/sct|228366006"
#         },
#         {
#           "type": {
#             "coding": [
#               {
#                 "system": "http://vzvz.nl/fhir/CodeSystem/TaskParameterType",
#                 "code": "query_string"
#               }
#             ]
#           },
#           "valueString": "Observation?code=http://snomed.info/sct|228273003"
#         },
#         {
#           "type": {
#             "coding": [
#               {
#                 "system": "http://vzvz.nl/fhir/CodeSystem/TaskParameterType",
#                 "code": "query_string"
#               }
#             ]
#           },
#           "valueString": "Observation?code=http://snomed.info/sct|365980008"
#         },
#         {
#           "type": {
#             "coding": [
#               {
#                 "system": "http://vzvz.nl/fhir/CodeSystem/TaskParameterType",
#                 "code": "query_string"
#               }
#             ]
#           },
#           "valueString": "NutritionOrder"
#         },
#         {
#           "type": {
#             "coding": [
#               {
#                 "system": "http://vzvz.nl/fhir/CodeSystem/TaskParameterType",
#                 "code": "query_string"
#               }
#             ]
#           },
#           "valueString": "Flag"
#         },
#         {
#           "type": {
#             "coding": [
#               {
#                 "system": "http://vzvz.nl/fhir/CodeSystem/TaskParameterType",
#                 "code": "query_string"
#               }
#             ]
#           },
#           "valueString": "AllergyIntolerance"
#         },
#         {
#           "type": {
#             "coding": [
#               {
#                 "system": "http://vzvz.nl/fhir/CodeSystem/TaskParameterType",
#                 "code": "query_string"
#               }
#             ]
#           },
#           "valueString": "MedicationStatement?category=urn:oid:2.16.840.1.113883.2.4.3.11.60.20.77.5.3|6&_include=MedicationStatement:medication"
#         },
#         {
#           "type": {
#             "coding": [
#               {
#                 "system": "http://vzvz.nl/fhir/CodeSystem/TaskParameterType",
#                 "code": "query_string"
#               }
#             ]
#           },
#           "valueString": "MedicationRequest?category=http://snomed.info/sct|16076005&_include=MedicationRequest:medication"
#         },
#         {
#           "type": {
#             "coding": [
#               {
#                 "system": "http://vzvz.nl/fhir/CodeSystem/TaskParameterType",
#                 "code": "query_string"
#               }
#             ]
#           },
#           "valueString": "MedicationDispense?category=http://snomed.info/sct|422037009&_include=MedicationDispense:medication"
#         },
#         {
#           "type": {
#             "coding": [
#               {
#                 "system": "http://vzvz.nl/fhir/CodeSystem/TaskParameterType",
#                 "code": "query_string"
#               }
#             ]
#           },
#           "valueString": "DeviceUseStatement?_include=DeviceUseStatement:device"
#         },
#         {
#           "type": {
#             "coding": [
#               {
#                 "system": "http://vzvz.nl/fhir/CodeSystem/TaskParameterType",
#                 "code": "query_string"
#               }
#             ]
#           },
#           "valueString": "Immunization?status=completed"
#         },
#         {
#           "type": {
#             "coding": [
#               {
#                 "system": "http://vzvz.nl/fhir/CodeSystem/TaskParameterType",
#                 "code": "query_string"
#               }
#             ]
#           },
#           "valueString": "Observation/$lastn?code=http://loinc.org|85354-9"
#         },
#         {
#           "type": {
#             "coding": [
#               {
#                 "system": "http://vzvz.nl/fhir/CodeSystem/TaskParameterType",
#                 "code": "query_string"
#               }
#             ]
#           },
#           "valueString": "Observation/$lastn?code=http://loinc.org|29463-7"
#         },
#         {
#           "type": {
#             "coding": [
#               {
#                 "system": "http://vzvz.nl/fhir/CodeSystem/TaskParameterType",
#                 "code": "query_string"
#               }
#             ]
#           },
#           "valueString": "Observation/$lastn?code=http://loinc.org|8302-2,http://loinc.org|8306-3,http://loinc.org|8308-9"
#         },
#         {
#           "type": {
#             "coding": [
#               {
#                 "system": "http://vzvz.nl/fhir/CodeSystem/TaskParameterType",
#                 "code": "query_string"
#               }
#             ]
#           },
#           "valueString": "Observation/$lastn?category=http://snomed.info/sct|275711006&_include=Observation:related-target&_include=Observation:specimen"
#         },
#         {
#           "type": {
#             "coding": [
#               {
#                 "system": "http://vzvz.nl/fhir/CodeSystem/TaskParameterType",
#                 "code": "query_string"
#               }
#             ]
#           },
#           "valueString": "Procedure?category=http://snomed.info/sct|387713003"
#         },
#         {
#           "type": {
#             "coding": [
#               {
#                 "system": "http://vzvz.nl/fhir/CodeSystem/TaskParameterType",
#                 "code": "query_string"
#               }
#             ]
#           },
#           "valueString": "Encounter?class=http://hl7.org/fhir/v3/ActCode|IMP,http://hl7.org/fhir/v3/ActCode|ACUTE,http://hl7.org/fhir/v3/ActCode|NONAC"
#         },
#         {
#           "type": {
#             "coding": [
#               {
#                 "system": "http://vzvz.nl/fhir/CodeSystem/TaskParameterType",
#                 "code": "query_string"
#               }
#             ]
#           },
#           "valueString": "ProcedureRequest?status=active"
#         },
#         {
#           "type": {
#             "coding": [
#               {
#                 "system": "http://vzvz.nl/fhir/CodeSystem/TaskParameterType",
#                 "code": "query_string"
#               }
#             ]
#           },
#           "valueString": "ImmunizationRecommendation"
#         },
#         {
#           "type": {
#             "coding": [
#               {
#                 "system": "http://vzvz.nl/fhir/CodeSystem/TaskParameterType",
#                 "code": "query_string"
#               }
#             ]
#           },
#           "valueString": "MedicationDispense?category=http://snomed.info/sct|422037009&status=in-progress,preparation&_include=MedicationDispense:medication"
#         },
#         {
#           "type": {
#             "coding": [
#               {
#                 "system": "http://vzvz.nl/fhir/CodeSystem/TaskParameterType",
#                 "code": "query_string"
#               }
#             ]
#           },
#           "valueString": "DeviceRequest?status=active&_include=DeviceRequest:device"
#         },
#         {
#           "type": {
#             "coding": [
#               {
#                 "system": "http://vzvz.nl/fhir/CodeSystem/TaskParameterType",
#                 "code": "query_string"
#               }
#             ]
#           },
#           "valueString": "Appointment?status=booked,pending,proposed"
#         },
#         {
#           "type": {
#             "coding": [
#               {
#                 "system": "http://vzvz.nl/fhir/CodeSystem/TaskParameterType",
#                 "code": "query_string"
#               }
#             ]
#           },
#           "valueString": "DocumentReference?status=current&indexed=ge2022-01-01"
#         }
#       ]
#     })
#     return task_aof

# # -------------
# # - Nuts Node -
# # -------------

# def call_node_search_receiver(did_receiver):
#     endpoint = f"{BASE_URL_NUTS_NODE}/internal/vcr/v2/issuer/vc/search?credentialType=VzvzUraCredential&issuer={did_receiver}"

#     request_body = {}
#     headers = {}

#     response = requests.get(endpoint, data=request_body, headers=headers)
#     response.raise_for_status()
#     print('response.text: ' + response.text)

# def call_node_search_sender(did_sender):
#     endpoint = f"{BASE_URL_NUTS_NODE}/internal/vcr/v2/issuer/vc/search?credentialType=VzvzUraCredential&issuer={did_sender}"

#     request_body = {}
#     headers = {}

#     response = requests.get(endpoint, data=request_body, headers=headers)
#     response.raise_for_status()
#     print('response.text: ' + response.text)

# def call_node_introspect(access_token):
#     """
#     Introspects an access token to determine its validity.
#     Args:
#         access_token (str): The access token to introspect.
#     Returns:
#         dict: A dictionary containing information about the access token if it is valid.
#     Raises:
#         Exception: If the introspection request fails or the token is invalid.
#     """
#     endpoint = f"{BASE_URL_NUTS_NODE}/internal/auth/v1/accesstoken/introspect"
#     request_body = { "token" : f"{access_token}" }
#     headers = {'Content-Type': 'application/x-www-form-urlencoded'}

#     #we need an exception handler here for
#     response = requests.post(endpoint, data=request_body, headers=headers)

#     if response.status_code == 200:
#         return response.json()
#     else:
#         raise Exception(f"Introspection failed with status code {response.status_code}: {response.text}")
#         return False

# # -------
# # - LSP -
# # -------

# def call_lsp_get_routing_info():
#     endpoint = f"{BASE_URL_LSP}/adresseringservice/getRoutingInfo"

#     ura = '90001235' # TODO

#     request_body = '{"destination":{"code":"' + ura + '","codeSystem":"urn:oid:2.16.528.1.1007.3.3"},"interaction":[{"id":"create:Task:2.0:request"}]}'
#     headers = {
#       'AORTA-ID': 'initialRequestID=f4857f0d-2c3a-439a-9b38-0382e5417396; requestID=ba483d8f-d3b1-4b75-b1e2-e36d59a6dc38',
#       'Content-Type': 'application/json; charset=utf-8'
#     }
#     cert = ('LSP110.csc-lsp.nl.pem', 'LSP110.csc-lsp.nl.key.unencrypted') # TODO

#     response = requests.post(endpoint, data=request_body, headers=headers, verify=False, cert=cert)
#     response.raise_for_status()
#     response_json = response.json()
#     lsp_application_id = response_json[0]["destinationInfo"][0]["destination"]["code"]
#     print('lsp_application_id:' + lsp_application_id)

# def call_lsp_token_exchange_request():
#     endpoint = f"{BASE_URL_LSP}/token"

#     lsp_application_id = '80000002' # TODO

#     f = open("transactietoken.txt", "rb")
#     transactie_token_b64_bytes = base64.b64encode(f.read())
#     transactie_token_b64 = transactie_token_b64_bytes.decode()
#     transactie_token_b64_url = urllib.parse.quote(transactie_token_b64)
#     f.close()
#     #print('transactie_token_b64_url:'+transactie_token_b64_url)

#     request_body = 'grant_type=urn%3Aietf%3Aparams%3Aoauth%3Agrant-type%3Atoken-exchange&client_id=urn%3Aoid%3A2.16.840.1.113883.2.4.6.6.110&audience=urn%3Aoid%3A2.16.840.1.113883.2.4.6.6.' + lsp_application_id + '&requested_token_type=urn%3Aietf%3Aparams%3Aoauth%3Atoken-type%3Ajwt&subject_token=' + transactie_token_b64_url + '&subject_token_type=urn%3Aietf%3Aparams%3Aoauth%3Atoken-type%3Asaml2&scope=create%3ATask%3A2.0%3Arequest~aorta.contextcode.BGZ~normaal'
#     headers = {
#       'AORTA-ID': 'initialRequestID=4260560a-e506-4c13-a8a2-276e26bcc599; requestID=adfe821e-086f-4cff-89a5-0cf11f1e941c',
#       'Content-Type': 'application/x-www-form-urlencoded'
#     }
#     cert = ('LSP110.csc-lsp.nl.pem', 'LSP110.csc-lsp.nl.key.unencrypted')

#     response = requests.post(endpoint, data=request_body, headers=headers, verify=False, cert=cert)
#     response.raise_for_status()
#     response_json = response.json()
#     access_token = response_json["access_token"]
#     return access_token

# def call_lsp_create_task(task_aof):
#     endpoint = f"{BASE_URL_LSP}/rbvnc/fhir/r4/Task"

#     request_body = task_aof
#     headers = {
#       'Authorization': 'Bearer ' + access_token,
#       'AORTA-ID': 'initialRequestID=8ce9adde-7d32-49c5-b2b4-637aa4aca141; requestID=174ebcb2-ebf4-4eff-87bc-3e9584ae424c',
#       'AORTA-Version': 'contentVersion=1.0; acceptVersion=1.x',
#       'Content-Type': 'application/fhir+json'
#     }
#     cert = ('LSP110.csc-lsp.nl.pem', 'LSP110.csc-lsp.nl.key.unencrypted')

#     response = requests.post(endpoint, data=request_body, headers=headers, verify=False, cert=cert)
#     #response.raise_for_status()
#     print(response.text)

# # ------------------
# # - Initialization -
# # ------------------

# class S(BaseHTTPRequestHandler):
#     def _set_response(self):
#         if (self.path == "/internal/auth/v1/request-access-token"):
#             request_access_token(self)
#         elif (self.path == "/Task"):
#             create_task(self)
#         else:
#             self.send_response(501)
#             self.send_header('Content-Type', 'application/json')
#             self.end_headers()
#             self.wfile.write('')

#     def do_GET(self):
#         print("GET request,\n\nPath: " + str(self.path) + "\n\nHeaders:\n" + str(self.headers) + "\n")
#         self._set_response()

#     def do_POST(self):
#         print("POST request\n\nPath:" + str(self.path) + "\n\nHeaders:\n" + str(self.headers) + "\n")
#         self._set_response()

# def run(server_class=HTTPServer, handler_class=S):
#     """Entrypoint for python server"""
#     server_address = ("0.0.0.0", 8000)
#     httpd = server_class(server_address, handler_class)
#     print("launching server...")
#     httpd.serve_forever()

# if __name__ == "__main__":
#     run()
