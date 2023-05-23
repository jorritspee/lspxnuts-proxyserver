from flask import current_app
import json

class Aorta_notification_transformer:
    def transform_notification(task_ta_np_json):
        """2.16 transform notification"""
        task_aof = json.dumps({
      "resourceType": "Task",
      "id": "nl-vzvz-TaskNotifiedPull-request-example",
      "meta": {
        "profile": [
          "http://vzvz.nl/fhir/StructureDefinition/nl-vzvz-TaskNotifiedPull"
        ]
      },
      "contained": [
        {
          "resourceType": "Device",
          "id": "device1",
          "meta": {
            "profile": [
              "http://vzvz.nl/fhir/StructureDefinition/nl-vzvz-Device"
            ]
          },
          "identifier": [
            {
              "system": "http://fhir.nl/fhir/NamingSystem/aorta-app-id",
              "value": "110"
            }
          ],
          "deviceName": [
            {
              "name": "TestApplicatie",
              "type": "user-friendly-name"
            }
          ],
          "owner": {
            "identifier": {
              "system": "http://fhir.nl/fhir/NamingSystem/ura",
              "value": "90000380"
            }
          }
        }
      ],
      "status": "requested",
      "intent": "proposal",
      "code": {
        "coding": [
          {
            "system": "http://vzvz.nl/fhir/CodeSystem/aorta-taskcode",
            "code": "notified_pull"
          }
        ]
      },
      "for": {
        "identifier": {
          "system": "http://fhir.nl/fhir/NamingSystem/bsn",
          "value": "012345672"
        }
      },
      "requester": {
        "reference": "#device1",
        "type": "Device"
      },
      "owner": {
        "identifier": {
          "system": "http://fhir.nl/fhir/NamingSystem/ura",
          "value": "90000380"
        }
      },
      "restriction": {
        "period": {
          "end": "2023-05-05T12:00:00+02:00"
        }
      },
      "input": [
        {
          "type": {
            "coding": [
              {
                "system": "http://vzvz.nl/fhir/CodeSystem/TaskParameterType",
                "code": "consent_token"
              }
            ]
          },
          "valueString": "did:nuts:6AiKV8hQx5nMaSfLNByaxiBjN3XBEUx4LmiHh2iYwuYe"
        },
        {
          "type": {
            "coding": [
              {
                "system": "http://vzvz.nl/fhir/CodeSystem/TaskParameterType",
                "code": "query_string"
              }
            ]
          },
          "valueString": "Patient?_include=Patient:general-practitioner"
        },
        {
          "type": {
            "coding": [
              {
                "system": "http://vzvz.nl/fhir/CodeSystem/TaskParameterType",
                "code": "query_string"
              }
            ]
          },
          "valueString": "Coverage?_include=Coverage:payor:Patient&_include=Coverage:payor:Organization"
        },
        {
          "type": {
            "coding": [
              {
                "system": "http://vzvz.nl/fhir/CodeSystem/TaskParameterType",
                "code": "query_string"
              }
            ]
          },
          "valueString": "Consent?category=http://snomed.info/sct|11291000146105"
        },
        {
          "type": {
            "coding": [
              {
                "system": "http://vzvz.nl/fhir/CodeSystem/TaskParameterType",
                "code": "query_string"
              }
            ]
          },
          "valueString": "Consent?category=http://snomed.info/sct|11341000146107"
        },
        {
          "type": {
            "coding": [
              {
                "system": "http://vzvz.nl/fhir/CodeSystem/TaskParameterType",
                "code": "query_string"
              }
            ]
          },
          "valueString": "Observation/$lastn?category=http://snomed.info/sct|118228005,http://snomed.info/sct|384821006"
        },
        {
          "type": {
            "coding": [
              {
                "system": "http://vzvz.nl/fhir/CodeSystem/TaskParameterType",
                "code": "query_string"
              }
            ]
          },
          "valueString": "Condition"
        },
        {
          "type": {
            "coding": [
              {
                "system": "http://vzvz.nl/fhir/CodeSystem/TaskParameterType",
                "code": "query_string"
              }
            ]
          },
          "valueString": "Observation/$lastn?code=http://snomed.info/sct|365508006"
        },
        {
          "type": {
            "coding": [
              {
                "system": "http://vzvz.nl/fhir/CodeSystem/TaskParameterType",
                "code": "query_string"
              }
            ]
          },
          "valueString": "Observation?code=http://snomed.info/sct|228366006"
        },
        {
          "type": {
            "coding": [
              {
                "system": "http://vzvz.nl/fhir/CodeSystem/TaskParameterType",
                "code": "query_string"
              }
            ]
          },
          "valueString": "Observation?code=http://snomed.info/sct|228273003"
        },
        {
          "type": {
            "coding": [
              {
                "system": "http://vzvz.nl/fhir/CodeSystem/TaskParameterType",
                "code": "query_string"
              }
            ]
          },
          "valueString": "Observation?code=http://snomed.info/sct|365980008"
        },
        {
          "type": {
            "coding": [
              {
                "system": "http://vzvz.nl/fhir/CodeSystem/TaskParameterType",
                "code": "query_string"
              }
            ]
          },
          "valueString": "NutritionOrder"
        },
        {
          "type": {
            "coding": [
              {
                "system": "http://vzvz.nl/fhir/CodeSystem/TaskParameterType",
                "code": "query_string"
              }
            ]
          },
          "valueString": "Flag"
        },
        {
          "type": {
            "coding": [
              {
                "system": "http://vzvz.nl/fhir/CodeSystem/TaskParameterType",
                "code": "query_string"
              }
            ]
          },
          "valueString": "AllergyIntolerance"
        },
        {
          "type": {
            "coding": [
              {
                "system": "http://vzvz.nl/fhir/CodeSystem/TaskParameterType",
                "code": "query_string"
              }
            ]
          },
          "valueString": "MedicationStatement?category=urn:oid:2.16.840.1.113883.2.4.3.11.60.20.77.5.3|6&_include=MedicationStatement:medication"
        },
        {
          "type": {
            "coding": [
              {
                "system": "http://vzvz.nl/fhir/CodeSystem/TaskParameterType",
                "code": "query_string"
              }
            ]
          },
          "valueString": "MedicationRequest?category=http://snomed.info/sct|16076005&_include=MedicationRequest:medication"
        },
        {
          "type": {
            "coding": [
              {
                "system": "http://vzvz.nl/fhir/CodeSystem/TaskParameterType",
                "code": "query_string"
              }
            ]
          },
          "valueString": "MedicationDispense?category=http://snomed.info/sct|422037009&_include=MedicationDispense:medication"
        },
        {
          "type": {
            "coding": [
              {
                "system": "http://vzvz.nl/fhir/CodeSystem/TaskParameterType",
                "code": "query_string"
              }
            ]
          },
          "valueString": "DeviceUseStatement?_include=DeviceUseStatement:device"
        },
        {
          "type": {
            "coding": [
              {
                "system": "http://vzvz.nl/fhir/CodeSystem/TaskParameterType",
                "code": "query_string"
              }
            ]
          },
          "valueString": "Immunization?status=completed"
        },
        {
          "type": {
            "coding": [
              {
                "system": "http://vzvz.nl/fhir/CodeSystem/TaskParameterType",
                "code": "query_string"
              }
            ]
          },
          "valueString": "Observation/$lastn?code=http://loinc.org|85354-9"
        },
        {
          "type": {
            "coding": [
              {
                "system": "http://vzvz.nl/fhir/CodeSystem/TaskParameterType",
                "code": "query_string"
              }
            ]
          },
          "valueString": "Observation/$lastn?code=http://loinc.org|29463-7"
        },
        {
          "type": {
            "coding": [
              {
                "system": "http://vzvz.nl/fhir/CodeSystem/TaskParameterType",
                "code": "query_string"
              }
            ]
          },
          "valueString": "Observation/$lastn?code=http://loinc.org|8302-2,http://loinc.org|8306-3,http://loinc.org|8308-9"
        },
        {
          "type": {
            "coding": [
              {
                "system": "http://vzvz.nl/fhir/CodeSystem/TaskParameterType",
                "code": "query_string"
              }
            ]
          },
          "valueString": "Observation/$lastn?category=http://snomed.info/sct|275711006&_include=Observation:related-target&_include=Observation:specimen"
        },
        {
          "type": {
            "coding": [
              {
                "system": "http://vzvz.nl/fhir/CodeSystem/TaskParameterType",
                "code": "query_string"
              }
            ]
          },
          "valueString": "Procedure?category=http://snomed.info/sct|387713003"
        },
        {
          "type": {
            "coding": [
              {
                "system": "http://vzvz.nl/fhir/CodeSystem/TaskParameterType",
                "code": "query_string"
              }
            ]
          },
          "valueString": "Encounter?class=http://hl7.org/fhir/v3/ActCode|IMP,http://hl7.org/fhir/v3/ActCode|ACUTE,http://hl7.org/fhir/v3/ActCode|NONAC"
        },
        {
          "type": {
            "coding": [
              {
                "system": "http://vzvz.nl/fhir/CodeSystem/TaskParameterType",
                "code": "query_string"
              }
            ]
          },
          "valueString": "ProcedureRequest?status=active"
        },
        {
          "type": {
            "coding": [
              {
                "system": "http://vzvz.nl/fhir/CodeSystem/TaskParameterType",
                "code": "query_string"
              }
            ]
          },
          "valueString": "ImmunizationRecommendation"
        },
        {
          "type": {
            "coding": [
              {
                "system": "http://vzvz.nl/fhir/CodeSystem/TaskParameterType",
                "code": "query_string"
              }
            ]
          },
          "valueString": "MedicationDispense?category=http://snomed.info/sct|422037009&status=in-progress,preparation&_include=MedicationDispense:medication"
        },
        {
          "type": {
            "coding": [
              {
                "system": "http://vzvz.nl/fhir/CodeSystem/TaskParameterType",
                "code": "query_string"
              }
            ]
          },
          "valueString": "DeviceRequest?status=active&_include=DeviceRequest:device"
        },
        {
          "type": {
            "coding": [
              {
                "system": "http://vzvz.nl/fhir/CodeSystem/TaskParameterType",
                "code": "query_string"
              }
            ]
          },
          "valueString": "Appointment?status=booked,pending,proposed"
        },
        {
          "type": {
            "coding": [
              {
                "system": "http://vzvz.nl/fhir/CodeSystem/TaskParameterType",
                "code": "query_string"
              }
            ]
          },
          "valueString": "DocumentReference?status=current&indexed=ge2022-01-01"
        }
      ]
    })
        return task_aof
    
