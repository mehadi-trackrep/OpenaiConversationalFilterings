#!/usr/bin/env bash
lambda_name=OpenAIConversationalFilterings

home=$(pwd)

rm ${lambda_name}.zip

cd venv/lib/python3.*/site-packages

zip -r9 ${lambda_name}.zip * -x \*boto*\*
mv ${lambda_name}.zip "$home"

cd "$home"

zip -g -r ${lambda_name}.zip * -x \*venv\* \*unit_tests\* lambda_unit_test.py *.txt *.sh *.pth *.egg

aws lambda update-function-code \
    --function-name ${lambda_name} \
    --zip-file fileb://${lambda_name}.zip

rm ${lambda_name}.zip