from flask import current_app
import json, requests

class Nuts_vcr_client:
    def getURA(did = "did:nuts:EwVMYK2ugaMvRHUbGFBhuyF423JuNQbtpes35eHhkQic"):
        ura = False

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
            ura = response.json()["verifiableCredentials"][0]["verifiableCredential"]["credentialSubject"]["nuts:ura"]
            return ura
        except:
            return False