import os
import time
import json
import openai
import traceback
from clients import OpenAIChatClient
from loguru import logger as LOGGER


PROJECT_DIR = f"{os.path.dirname(__file__)}/"


def run():
    chat_context_path = f'{PROJECT_DIR.rstrip("/")}/contexts/context1.txt'
    result_path = f'{PROJECT_DIR.rstrip("/")}/results/result1.json'
    LOGGER.debug(f"chat_context_path: {chat_context_path}\nresult_path: {result_path}")
    result = {
        "f1": "v1",
        "f2": "v2"
    }
    rfile = open(chat_context_path, 'r')
    content = rfile.read()
    rfile.close()
    print(f"ctx: {content}")
    
    wfile = open(result_path, 'w')
    wfile.write(json.dumps(result))
    


run()