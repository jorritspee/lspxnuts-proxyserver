from flask import current_app
import json

class Aorta_notification_transformer:
    def transform_notification(source_task):
        """2.16 transform notification"""
        target_task_code = {}
        target_task_for = {}
        target_task_device = {}
        target_task_owner = {}
        target_task_restriction = {}
        target_task_input = []
        # --------
        # - code -
        # --------
        try:
            #source_task_code_coding_system = source_task['code']['coding'][0]['system']
            #source_task_code_coding_code = source_task['code']['coding'][0]['code']
            target_task_code = {
                "coding": [
                    {
                        "system": "http://vzvz.nl/fhir/CodeSystem/aorta-taskcode",
                        "code": "notified_pull"
                    }
                ]
            }
        except:
            print('Error mapping code')
        # -------
        # - for -
        # -------
        try:
            source_task_for_identifier_system = source_task['for']['identifier']['system']
            source_task_for_identifier_value = source_task['for']['identifier']['value']
            target_task_for = {
                "identifier": {
                    "system": f"{source_task_for_identifier_system}",
                    "value": f"{source_task_for_identifier_value}"
                }
            }
        except:
            print('Error mapping for')
        # ----------------------
        # - contained (Device) -
        # ----------------------
        try:
            source_task_requester_agent_identifier_system = source_task['requester']['agent']['identifier']['system']
            source_task_requester_agent_identifier_value = source_task['requester']['agent']['identifier']['value']
            source_task_requester_onbehalfof_identifier_system = source_task['requester']['onBehalfOf']['identifier']['system']
            source_task_requester_onbehalfof_identifier_value = source_task['requester']['onBehalfOf']['identifier']['value']
            target_task_device = {
                "resourceType": "Device",
                "id": "device1",
                "meta": {
                    "profile": [
                        "http://vzvz.nl/fhir/StructureDefinition/nl-vzvz-Device"
                    ]
                },
                "identifier": [
                    {
                        "system": f"{source_task_requester_agent_identifier_system}",
                        "value": f"{source_task_requester_agent_identifier_value}"
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
                        "system": f"{source_task_requester_onbehalfof_identifier_system}",
                        "value": f"{source_task_requester_onbehalfof_identifier_value}"
                    }
                }
            }
        except:
            print('Error mapping contained (Device)')
        # ---------
        # - owner -
        # ---------
        try:
            source_task_owner_identifier_system = source_task['owner']['identifier']['system']
            source_task_owner_identifier_value = source_task['owner']['identifier']['value']
            target_task_owner = {
                "identifier": {
                    "system": f"{source_task_owner_identifier_system}",
                    "value": f"{source_task_owner_identifier_value}"
                }
            }
        except:
            print('Error mapping owner')        
        # ---------------
        # - restriction -
        # ---------------
        try:
            source_task_restriction_period_end = source_task['restriction']['period']['end']
            target_task_restriction = {
                "period": {
                    "end": f"{source_task_restriction_period_end}"
                }
            }
        except:
            print('Error mapping restriction') 
        # ---------
        # - input -
        # ---------
        try:
            target_task_input = [];
            for source_task_input_item in source_task['input']:
                if source_task_input_item['type']['coding'][0]['code'] == 'authorization_base':
                    # ----------------------
                    # - authorization_base -
                    # ----------------------
                    source_task_input_item_valueString = source_task_input_item['valueString']
                    target_task_input_item = {
                        "type": {
                            "coding": [
                                {
                                    "system": "http://vzvz.nl/fhir/CodeSystem/TaskParameterType",
                                    "code": "consent_token"
                                }
                            ]
                        },
                        "valueString": f"{source_task_input_item_valueString}"
                    }
                    target_task_input.append(target_task_input_item)
                elif source_task_input_item['type']['coding'][0]['code'] == 'query_resource' or source_task_input_item['type']['coding'][0]['code'] == '79191-3':
                    # ------------------
                    # - query_resource -
                    # ------------------
                    source_task_input_item_valueString = source_task_input_item['valueString']
                    target_task_input_item = {
                        "type": {
                            "coding": [
                                {
                                    "system": "http://vzvz.nl/fhir/CodeSystem/TaskParameterType",
                                    "code": "query_string"
                                }
                            ]
                        },
                        "valueString": f"{source_task_input_item_valueString}"
                    }
                    target_task_input.append(target_task_input_item)
        except:
            print('Error mapping input')
        # --------
        # - Task -
        # --------
        target_task = {
            "resourceType": "Task",
            "id": "nl-vzvz-TaskNotifiedPull-request-example",
            "meta": {
                "profile": [
                    "http://vzvz.nl/fhir/StructureDefinition/nl-vzvz-TaskNotifiedPull"
                    ]
                },
            "contained": [
                target_task_device
            ],
            "status": "requested",
            "intent": "proposal",
            "code": target_task_code,
            "for": target_task_for,
            "requester": {
                "reference": "#device1",
                "type": "Device"
            },
            "owner": target_task_owner,
            "restriction": target_task_restriction,
            "input": target_task_input
        }
        return json.dumps(target_task)
