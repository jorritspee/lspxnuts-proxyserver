from flask import current_app
import json, requests

class Nuts_vcr_client:
    def getURA(did):
        endpoint = f"{current_app.config['BASE_URL_NUTS_NODE']}/internal/vcr/v2/search"

        json_obj =  {
                        "query": {
                            "@context": [
                                "https://www.w3.org/2018/credentials/v1",
                                "https://nuts.nl/credentials/v1"
                            ],
                            "type": [
                                "VerifiableCredential",
                                "VzvzUraCredential"
                            ],
                            "credentialSubject": {
                                "id": did
                            }
                        },
                        "searchOptions": {
                            "allowUntrustedIssuer": True
                        }
                    }

        headers = {
        'Content-Type': 'application/json'
        }

        try:
            response = requests.post(endpoint, json=json_obj, headers=headers)
        except:
            print("error sending vcr request to nuts node api")
            return False

        try:
            credentials = response.json()
            for credential in credentials['verifiableCredentials']:
                if "VzvzUraCredential" in credential["verifiableCredential"]["type"]:
                    return credential["verifiableCredential"]["credentialSubject"]["schema:identifier"]
            return False

        except:
            return False
