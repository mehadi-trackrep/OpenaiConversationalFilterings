import os

API = {
    '/prospector-list': 'ProspectorListDev-g2' # lambda names
}

openai_api_key=os.environ.get('OPENAI_API_KEY', default=None)
MODEL=os.environ.get('MODEL', default="gpt-4") # "gpt-4-turbo-preview"

params = {
    "path": {},
    "querystring": {},
    "header": {
        "goava-env": "production",
        "Host": "hekd0k0m85.execute-api.eu-west-1.amazonaws.com",
        "X-Forwarded-For": "114.134.91.102",
        "X-Forwarded-Proto": "https"
    }
}
context = {
    "http-method": "POST",
    "resource-path": "/prospector-list",
    "lambda-env": "prod"
}