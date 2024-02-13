import json
import boto3
from loguru import logger

def to_json(data, indent=2):
    return json.dumps(data, ensure_ascii=False, indent=indent, default=str)

def invoke_lambda(lambda_function, payload):
    lambda_client = boto3.client('lambda')
    logger.info(f"\nPayload: {json.dumps(payload)}\n")
    response = None
    
    try:
        resp = lambda_client.invoke(
            FunctionName=lambda_function #'prod--global-event-dispatcher',
            ,InvocationType='RequestResponse' #'Event'
            ,Payload=json.dumps(payload)
        )
        response = json.loads(resp["Payload"].read())
    except Exception as e:
        logger.error(f"Exception: {e}")
    
    return response