import os
import time
import json
import openai
import traceback
from clients import OpenAIChatClient
from loguru import logger as LOGGER
from config import MODEL, openai_api_key


openai.api_key = openai_api_key
PROJECT_DIR = f"{os.path.dirname(__file__)}/"

def estimate_costs(total_completion_tokens, total_prompt_tokens, model="gpt4"):
    if model == "gpt4":
        input_cost = (total_prompt_tokens/1000) * 0.03
        output_cost = (total_completion_tokens/1000) * 0.06
        total_cost = input_cost + output_cost
        LOGGER.info(f"\n##Total estimated costs using {model}: ${total_cost}\n")

    elif model == "gpt3":
        ...


def start_openai_invocation_process(question: str) -> dict:
    chat_context_path = f'{PROJECT_DIR.rstrip("/")}/contexts/context2.txt'
    # result_path = f'{PROJECT_DIR.rstrip("/")}/results/result2.json'
    rfile = open(chat_context_path, 'r')
    chat_context = rfile.read()
    rfile.close()
    
    result = {}
    
    openai_chat_obj = OpenAIChatClient(
        chat_context=chat_context
        ,model=MODEL
    )
    try:
        result = openai_chat_obj.process_the_given_question(
            [
                question
            ]
        )
        LOGGER.info("prompt_tokens: {}; completion_tokens: {}; total_tokens: {}\n".format(
            openai_chat_obj.prompt_tokens, 
            openai_chat_obj.completion_tokens, 
            openai_chat_obj.prompt_tokens + openai_chat_obj.completion_tokens)
        )
    except Exception as _:
        print("Exception2: {}".format(traceback.format_exc()))

    LOGGER.info("Now estimating the costs after processing the targeted questions..")
    estimate_costs(openai_chat_obj.completion_tokens, openai_chat_obj.prompt_tokens)

    return json.loads(result)