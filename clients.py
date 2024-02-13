import json
import openai
import traceback
from loguru import logger as LOGGER


class OpenAIChatClient:
    def __init__(self, chat_context: str, model='gpt-4'):
        self.chat_context = chat_context
        self.model = model
        self.completion_tokens = 0
        self.prompt_tokens = 0
    

    def get_response(self, context):

        response = openai.ChatCompletion.create(
            model=self.model #"gpt-4", # "gpt-4-turbo-preview"
            ,messages=[
                {"role": "system", "content": "You are a helpful assistant."},
                {"role": "user", "content": context}
            ]
        )
        
        content = response["choices"][0]["message"]["content"]
        completion_tokens = response['usage']['completion_tokens']
        prompt_tokens = response['usage']['prompt_tokens']

        self.completion_tokens += completion_tokens
        self.prompt_tokens += prompt_tokens
        
        ##print("prompt_tokens: {}\ncompletion_tokens: {}\n".format(self.prompt_tokens, self.completion_tokens))
        return content


    def process_the_given_question(self, question) -> str:
        LOGGER.info(f"==> Question: {question}")
        response_content = ""
        try:
            context = self.chat_context + "\n".join(
                [
                    f"Q {question}" for question in question
                ]
            )
            response_content = self.get_response(context).strip()
            
            LOGGER.info("response_content: {}".format(json.dumps(json.loads(response_content), indent=4)))
        except Exception as _:
            print("Exception when processing question: {}".format(traceback.format_exc()))
            # for question in questions:
            #     self.csv_writer.writerow([f'{question}', 'FAILED_DURING_PROCESS', 'FAILED_DURING_PROCESS'])
        finally:
            ...
        return response_content
