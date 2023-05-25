from flask import jsonify, request, current_app
from flask_restful import Resource

class Fhir(Resource):
  
    # corresponds to the GET request.
    # this function is called whenever there
    # is a GET request for this resource
    def get(self):
        return {
    "resourceType": "Patient",
    "id": "zib-languageproficiency-example",
    "meta": {
        "profile":  [
            "http://fhir.nl/fhir/StructureDefinition/nl-core-patient"
        ]
    },
    "identifier":  [
        {
            "use": "official",
            "system": "http://fhir.nl/fhir/NamingSystem/bsn",
            "value": "999911120"
        }
    ],
    "active": True,
    "name":  [
        {
            "extension":  [
                {
                    "url": "http://hl7.org/fhir/StructureDefinition/humanname-assembly-order",
                    "valueCode": "NL4"
                }
            ],
            "use": "official",
            "family": "XXX_Helleman",
            "_family": {
                "extension":  [
                    {
                        "url": "http://hl7.org/fhir/StructureDefinition/humanname-own-name",
                        "valueString": "XXX_Verweij"
                    }
                ]
            },
            "given":  [
                "Alex",
                "A."
            ],
            "_given":  [
                {
                    "extension":  [
                        {
                            "url": "http://hl7.org/fhir/StructureDefinition/iso21090-EN-qualifier",
                            "valueCode": "CL"
                        }
                    ]
                },
                {
                    "extension":  [
                        {
                            "url": "http://hl7.org/fhir/StructureDefinition/iso21090-EN-qualifier",
                            "valueCode": "IN"
                        }
                    ]
                }
            ]
        }
    ],
    "telecom":  [
        {
            "system": "phone",
            "value": "06-12345678",
            "use": "mobile"
        },
        {
            "system": "email",
            "value": "XXX_Helleman@hotmail.com",
            "use": "home"
        }
    ],
    "gender": "male",
    "birthDate": "1964-08-02",
    "deceasedBoolean": False,
    "address":  [
        {
            "extension":  [
                {
                    "url": "http://fhir.nl/fhir/StructureDefinition/nl-core-address-official",
                    "valueBoolean": True
                }
            ],
            "use": "home",
            "type": "both",
            "line":  [
                "Knolweg 1020"
            ],
            "_line":  [
                {
                    "extension":  [
                        {
                            "url": "http://hl7.org/fhir/StructureDefinition/iso21090-ADXP-streetName",
                            "valueString": "Knolweg"
                        },
                        {
                            "url": "http://hl7.org/fhir/StructureDefinition/iso21090-ADXP-houseNumber",
                            "valueString": "1020"
                        }
                    ]
                }
            ],
            "city": "Stitswerd",
            "district": "Nederland",
            "postalCode": "9999XB",
            "country": "NLD"
        }
    ],
    "maritalStatus": {
        "coding":  [
            {
                "system": "http://hl7.org/fhir/v3/MaritalStatus",
                "code": "M",
                "display": "Married"
            }
        ]
    },
    "multipleBirthBoolean": False,
    "contact":  [
        {
            "relationship":  [
                {
                    "coding":  [
                        {
                            "system": "urn:oid:2.16.840.1.113883.2.4.3.11.22.472",
                            "code": "1",
                            "display": "Eerste relatie/contactpersoon"
                        }
                    ]
                },
                {
                    "coding":  [
                        {
                            "system": "http://hl7.org/fhir/v3/RoleCode",
                            "code": "HUSB",
                            "display": "Husband"
                        }
                    ]
                }
            ],
            "name": {
                "extension":  [
                    {
                        "url": "http://hl7.org/fhir/StructureDefinition/humanname-assembly-order",
                        "valueCode": "NL4"
                    }
                ],
                "use": "official",
                "family": "van Molenaar van der Jutte",
                "_family": {
                    "extension":  [
                        {
                            "url": "http://hl7.org/fhir/StructureDefinition/humanname-own-prefix",
                            "valueString": "van"
                        },
                        {
                            "url": "http://hl7.org/fhir/StructureDefinition/humanname-own-name",
                            "valueString": "Molenaar"
                        },
                        {
                            "url": "http://hl7.org/fhir/StructureDefinition/humanname-partner-prefix",
                            "valueString": "van der"
                        },
                        {
                            "url": "http://hl7.org/fhir/StructureDefinition/humanname-partner-name",
                            "valueString": "Jutte"
                        }
                    ]
                },
                "given":  [
                    "Janni",
                    "J.P.M."
                ],
                "_given":  [
                    {
                        "extension":  [
                            {
                                "url": "http://hl7.org/fhir/StructureDefinition/iso21090-EN-qualifier",
                                "valueCode": "CL"
                            }
                        ]
                    },
                    {
                        "extension":  [
                            {
                                "url": "http://hl7.org/fhir/StructureDefinition/iso21090-EN-qualifier",
                                "valueCode": "IN"
                            }
                        ]
                    }
                ]
            },
            "telecom":  [
                {
                    "system": "phone",
                    "value": "06-12345645",
                    "use": "mobile"
                },
                {
                    "system": "email",
                    "value": "j.vanderjutte@example.com"
                }
            ],
            "address": {
                "use": "home",
                "line":  [
                    "Knolweg 1020"
                ],
                "_line":  [
                    {
                        "extension":  [
                            {
                                "url": "http://hl7.org/fhir/StructureDefinition/iso21090-ADXP-streetName",
                                "valueString": "Knolweg"
                            },
                            {
                                "url": "http://hl7.org/fhir/StructureDefinition/iso21090-ADXP-houseNumber",
                                "valueString": "1020"
                            }
                        ]
                    }
                ],
                "city": "Sitswerd",
                "postalCode": "9999XB",
                "country": "Nederland"
            }
        }
    ],
    "communication":  [
        {
            "extension":  [
                {
                    "url": "http://nictiz.nl/fhir/StructureDefinition/patient-proficiency",
                    "extension":  [
                        {
                            "url": "languageProficiency",
                            "extension":  [
                                {
                                    "url": "level",
                                    "valueCoding": {
                                        "system": "http://terminology.hl7.org/CodeSystem/v3-LanguageAbilityProficiency",
                                        "code": "p",
                                        "display": "Poor"
                                    }
                                },
                                {
                                    "url": "type",
                                    "valueCoding": {
                                        "system": "http://terminology.hl7.org/CodeSystem/v3-LanguageAbilityMode",
                                        "code": "ESGN",
                                        "display": "Expressed signed"
                                    }
                                }
                            ]
                        },
                        {
                            "url": "http://nictiz.nl/fhir/StructureDefinition/patient-proficiency",
                            "extension":  [
                                {
                                    "url": "level",
                                    "valueCoding": {
                                        "system": "http://terminology.hl7.org/CodeSystem/v3-LanguageAbilityProficiency",
                                        "code": "p",
                                        "display": "Poor"
                                    }
                                },
                                {
                                    "url": "type",
                                    "valueCoding": {
                                        "system": "http://terminology.hl7.org/CodeSystem/v3-LanguageAbilityMode",
                                        "code": "ESP",
                                        "display": "Expressed spoken"
                                    }
                                }
                            ]
                        }
                    ]
                },
                {
                    "url": "http://nictiz.nl/fhir/StructureDefinition/Comment",
                    "valueString": "Bij gesprek met arts zoon uitnodigen voor vertalen"
                }
            ],
            "language": {
                "coding":  [
                    {
                        "system": "urn:ietf:bcp:47",
                        "code": "nl-NL",
                        "display": "Dutch (Netherlands)"
                    }
                ]
            },
            "preferred": True
        }
    ],
    "generalPractitioner":  [
        {
            "reference": "Practitioner/medmij-bgz-healthcareprovider-ts-02",
            "display": "Vaste Huisarts 1"
        }
    ]
}
    
    # Corresponds to POST request
    def post(self):
        return { "post not supported": "use GET"}, 405