.PHONY: start-local test coverage

APP_NAME=things_backend

start-local:
	uvicorn $(APP_NAME).main:app --reload

load-fixtures:
	poetry run load_fixtures

test:
ifdef filter
	poetry run pytest $(filter) -vv
else
	poetry run pytest -vv
endif

coverage: test
	poetry run pytest --cov-report term-missing --cov=$(APP_NAME)
