#!/bin/sh

echo '>> running migrations'
pipenv run python3 manage.py migrate
