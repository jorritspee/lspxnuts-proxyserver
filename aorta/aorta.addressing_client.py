from flask import current_app
import requests

class Aorta_addressing_client:
    def call_lsp_get_routing_info(ura_destination = "90001235"):
        endpoint = f"{current_app.config['BASE_URL_LSP']}/adresseringservice/getRoutingInfo"
        
        request_body = '{"destination":{"code":"' + ura_destination + '","codeSystem":"urn:oid:2.16.528.1.1007.3.3"},"interaction":[{"id":"create:Task:2.0:request"}]}'
        headers = {
        'AORTA-ID': 'initialRequestID=f4857f0d-2c3a-439a-9b38-0382e5417396; requestID=ba483d8f-d3b1-4b75-b1e2-e36d59a6dc38',
        'Content-Type': 'application/json; charset=utf-8'
        }
        cert = ('LSP110.csc-lsp.nl.pem', 'LSP110.csc-lsp.nl.key.unencrypted') # TODO
        
        response = requests.post(endpoint, data=request_body, headers=headers, verify=False, cert=cert)
        response.raise_for_status()
        response_json = response.json()
        lsp_application_id = response_json[0]["destinationInfo"][0]["destination"]["code"]
        print('lsp_application_id:' + lsp_application_id)

        return response_json