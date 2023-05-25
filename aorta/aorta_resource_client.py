from flask import current_app
import json, requests

class Aorta_resource_client:

    def call_lsp_create_task(task_aof, access_token):
        endpoint = f"{current_app.config['BASE_URL_LSP']}/rbvnc/fhir/r4/Task"
        
        request_body = task_aof
        headers = {
        'Authorization': 'Bearer ' + access_token,
        'AORTA-ID': 'initialRequestID=8ce9adde-7d32-49c5-b2b4-637aa4aca141; requestID=174ebcb2-ebf4-4eff-87bc-3e9584ae424c',
        'AORTA-Version': 'contentVersion=2.0; acceptVersion=2.x',
        'Content-Type': 'application/fhir+json'
        }
        cert = ('LSP110.csc-lsp.nl.pem', 'LSP110.csc-lsp.nl.key.unencrypted')
        
        response = requests.post(endpoint, data=request_body, headers=headers, verify=False, cert=cert)
        #response.raise_for_status()
        print("----BEGIN--------call_lsp_create_task, repsone.text: -------------")
        print(response.text)
        print("----END--------call_lsp_create_task, repsone.text: -------------")
        return response
