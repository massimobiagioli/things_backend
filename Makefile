.PHONY: help serve black isort flake8 bandit test coverage

default: help

APP_NAME=things_backend

help: # Show help for each of the Makefile recipes.
	@grep -E '^[a-zA-Z0-9 -]+:.*#'  Makefile | sort | while read -r l; do printf "\033[1;32m$$(echo $$l | cut -f 1 -d':')\033[00m:$$(echo $$l | cut -f 2- -d'#')\n"; done

serve:	# Start server
	poetry run uvicorn $(APP_NAME).main:app --reload

black:		# Run black
	poetry run black .

isort:		# Run isort
	poetry run isort .

flake8:		# Run flake8
	poetry run flake8 $(APP_NAME)

bandit:		# Run bandit
	poetry run bandit --ini .bandit

test:		# Run tests
ifdef filter
	poetry run pytest $(filter) -vv
else
	poetry run pytest -vv
endif

coverage: test	## Run tests with coverage
	poetry run pytest --cov-report term-missing --cov=$(APP_NAME)
