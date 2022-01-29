lint:
	@poetry run isort .
	@poetry run black . --exclude=.venv
	@poetry run flake8 --exclude=.venv

test:
	poetry run pytest . -s
