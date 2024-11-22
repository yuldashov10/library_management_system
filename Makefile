# Installing dependencies
install:
	poetry install

shell:
	poetry shell

# Linting and formatting
format:
	black .
	isort .

lint:
	flake8 .
	mypy .

# Running tests
test:
	pytest

# Full check (formatting, linting, tests)
check: format lint test

# Other commands
project_tree:
	tree -a -I ".venv|.git|.vscode|.idea|__pycache__"
