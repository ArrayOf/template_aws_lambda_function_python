#!/bin/bash

source activate

function_name="{{cookiecutter.function_name}}"
zip_file="function.zip"

aws lambda update-function-code --function-name "${function_name}" --zip-file "fileb://${zip_file}" --profile sofie --region sa-east-1

rm -rf "${zip_file}"