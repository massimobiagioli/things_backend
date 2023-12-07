.PHONY: help start-local black isort flake8 test coverage

default: help

APP_NAME=things_backend

help:           ## Show this help.
	@fgrep -h "##" $(MAKEFILE_LIST) | fgrep -v fgrep | sed -e 's/\\$$//' | sed -e 's/##//'

start-local:	## Start local server
	uvicorn $(APP_NAME).main:app --reload

black:		## Run black
	poetry run black .

isort:		## Run isort
	poetry run isort .

flake8:		## Run flake8
	poetry run flake8 $(APP_NAME)

test:		## Run tests
ifdef filter
	poetry run pytest $(filter) -vv
else
	poetry run pytest -vv
endif

coverage: test	## Run tests with coverage
	poetry run pytest --cov-report term-missing --cov=$(APP_NAME)
