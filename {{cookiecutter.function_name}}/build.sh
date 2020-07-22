#!/bin/bash

source activate

rm -rf function.zip

pip3 install --target ./.package -r src/requirements.txt

cd .package || exit

zip -r9 "${OLDPWD}"/function.zip .

cd "${OLDPWD}" || exit
cd src || exit

zip -r9 "${OLDPWD}"/function.zip .

cd "${OLDPWD}" || exit

rm -rf ./.package