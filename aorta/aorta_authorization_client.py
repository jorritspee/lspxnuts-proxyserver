from flask import current_app
import base64, urllib.parse, requests

class Aorta_authorization_client:

    def call_lsp_token_exchange_request(receiver_app_id, sender_application_id):
        endpoint = f"{current_app.config['BASE_URL_LSP']}/token"

        f = open(current_app.config["FILENAME_TRANSACTION_TOKEN"], "rb")
        transactie_token_b64_bytes = base64.b64encode(f.read())
        transactie_token_b64 = transactie_token_b64_bytes.decode()
        transactie_token_b64_url = urllib.parse.quote(transactie_token_b64)
        f.close()
        #print('transactie_token_b64_url:'+transactie_token_b64_url)

        request_body = 'grant_type=urn%3Aietf%3Aparams%3Aoauth%3Agrant-type%3Atoken-exchange&client_id=urn%3Aoid%3A2.16.840.1.113883.2.4.6.6.' + sender_application_id + '&audience=urn%3Aoid%3A2.16.840.1.113883.2.4.6.6.' + receiver_app_id + '&requested_token_type=urn%3Aietf%3Aparams%3Aoauth%3Atoken-type%3Ajwt&subject_token=' + transactie_token_b64_url + '&subject_token_type=urn%3Aietf%3Aparams%3Aoauth%3Atoken-type%3Asaml2&scope=create%3ATask%3A2.0%3Arequest~aorta.contextcode.BGZ~normaal'
        headers = {
        'AORTA-ID': 'initialRequestID=4260560a-e506-4c13-a8a2-276e26bcc599; requestID=adfe821e-086f-4cff-89a5-0cf11f1e941c',
        'Content-Type': 'application/x-www-form-urlencoded'
        }
        cert = ('LSP110.csc-lsp.nl.pem', 'LSP110.csc-lsp.nl.key.unencrypted')

        response = requests.post(endpoint, data=request_body, headers=headers, verify=False, cert=cert)
        response.raise_for_status()
        response_json = response.json()
        access_token = response_json["access_token"]
        return access_token
    
    def call_lsp_token_exchange_request_for_pull(receiver_app_id, sender_application_id):
        endpoint = f"{current_app.config['BASE_URL_LSP']}/token"

        f = open(current_app.config["FILENAME_TRANSACTION_TOKEN"], "rb")
        transactie_token_b64_bytes = base64.b64encode(f.read())
        transactie_token_b64 = transactie_token_b64_bytes.decode()
        transactie_token_b64_url = urllib.parse.quote(transactie_token_b64)
        f.close()
        #print('transactie_token_b64_url:'+transactie_token_b64_url)

        request_body = 'grant_type=urn%3Aietf%3Aparams%3Aoauth%3Agrant-type%3Atoken-exchange&client_id=urn%3Aoid%3A2.16.840.1.113883.2.4.6.6.' + receiver_app_id + '&audience=urn%3Aoid%3A2.16.840.1.113883.2.4.6.6.' + sender_application_id + '&requested_token_type=urn%3Aietf%3Aparams%3Aoauth%3Atoken-type%3Ajwt&subject_token=' + transactie_token_b64_url + '&subject_token_type=urn%3Aietf%3Aparams%3Aoauth%3Atoken-type%3Asaml2&scope=create%3ATask%3A2.0%3Arequest~aorta.contextcode.BGZ~normaal'
        headers = {
        'AORTA-ID': 'initialRequestID=4260560a-e506-4c13-a8a2-276e26bcc599; requestID=adfe821e-086f-4cff-89a5-0cf11f1e941c',
        'Content-Type': 'application/x-www-form-urlencoded'
        }
        cert = ('LSP110.csc-lsp.nl.pem', 'LSP110.csc-lsp.nl.key.unencrypted')

        response = requests.post(endpoint, data=request_body, headers=headers, verify=False, cert=cert)
        response.raise_for_status()
        response_json = response.json()
        access_token = response_json["access_token"]
        return access_token
