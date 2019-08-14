#!/bin/sh

. env/bin/activate
echo '>> running application'
pipenv run python3 manage.py run
