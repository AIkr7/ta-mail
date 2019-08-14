#!/bin/sh

setup:
	@echo 'initiating setup'
	@echo '>> installing required modules...'
	@sudo sh -c "apt install python3 python3-pip python3-venv;"
	@sudo sh -c "pip3 install pipenv --user"
	@echo '>> setup success!'

install:
	@echo 'initiating installation'
	@sh ./cmd/install.sh
	@echo '>> install success!'

run:
	@echo 'initiating application'
	@sh ./cmd/run.sh
	@echo '>> application terminated.'

migrate:
	@echo 'initiating migration'
	@sh ./cmd/migrate.sh
	@echo '>> migration success!'

push:
	@echo 'preparing your code to staging'
	# @sh ./cmd/push.sh
	@git push origin staging && heroku logs --tail --app proyekin-backend

all: install update migrate run

quick: update run

production:
	@python3 manage.py migrate
	@gunicorn backend.wsgi
