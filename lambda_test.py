import utils
import config
from lambda_function import lambda_handler


def run(event: dict): # full json payload
    return lambda_handler(event, None)    


if __name__ == "__main__":
    prospector_text = {
        "body-json": {
            "user_id": 571,
            "account_id": 3,
            "fields": [
                "orgno",
                "company_name"
            ],
            "question": "Finnish and Swedish Companies that deal with horse racing and earns more than 5 M euro and have less than 30 employees.",
            "from": 0,
            "size": 10
        },
        "params": config.params,
        "context": config.context
    }

    print(
        utils.to_json(
            run(prospector_text)
        )
    )