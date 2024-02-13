import utils
import time
import config
import traceback
from uuid import uuid4
from loguru import logger as LOGGER
from main import start_openai_invocation_process


def lambda_handler(event, _):
    LOGGER.info(utils.to_json(event))
    response_time = None
    try:
        resource = event["context"]["resource-path"]
        method = event["context"]["http-method"]
        lambda_env = event["context"]["lambda-env"]
        header = event["params"]["header"]
        body = event["body-json"]
        user_id = body.get('user_id')
        account_id = body.get('account_id')

        lambda_function_name = config.API[resource]        
        openai_result = start_openai_invocation_process(
            question=body.get('question')
        )
        
        del body['question']
        # add the filters from OpenAI response to the body
        body.update(openai_result)
        
        final_payload = {
            "body-json": body,
            "params": event["params"],
            "context": event["context"]
        }
        
        LOGGER.debug(f"--> body-json: {body}")
        
        t1 = time.perf_counter()
        response = utils.invoke_lambda(
            lambda_function=lambda_function_name
            ,payload=final_payload # it's internally converted to json
        )
        t2 = time.perf_counter()
        response_time = t2 - t1

        LOGGER.info(utils.to_json({
            "log_type": "metric", 
            "error": False,
            "response_time": response_time, 
            "response": response,
            "resource": resource, 
            "method": method, 
            "header": header, 
            "lambda_env": lambda_env, 
            "body-json": body
        }))

        return response
    except Exception as e:
        LOGGER.error(traceback.format_exc())
