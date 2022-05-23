.PHONY: fmt
fmt:
	@poetry run black . --exclude=.venv
	@poetry run isort .
	@poetry run flake8 --exclude=.venv

.PHONY: tests
tests:
	poetry run pytest . -s

.PHONY: packages
packages:
	poetry install

.PHONY: run
run:
	poetry run uvicorn src.infra.http.fastapi_server:app --port=8000 --reload
