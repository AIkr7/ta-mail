#!/bin/sh

echo '>> creating env...'
pipenv shell
echo '>> updating pip...'
pip3 install --upgrade pip
echo '>> installing dependencies...'
pipenv install --dev
echo '>> running migrations'
pipenv run python3 manage.py migrate