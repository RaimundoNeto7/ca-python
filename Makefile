lint:
	@poetry run isort .
	@poetry run black . --exclude=.venv
	@poetry run flake8 --exclude=.venv

test:
	poetry run pytest . -s

run:
	poetry run uvicorn src.infra.http.fastapi_server:app --port=8000 --reload
