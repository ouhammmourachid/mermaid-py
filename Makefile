.PHONY: install
install:
	poetry install

.PHONY: update
install:
	poetry update

.PHONY: build
build:
	poetry build

.PHONY: publish
publish:
	poetry publish

.PHONY: test
test:
	poetry run pytest

.PHONY: install-pre-commit
install-pre-commit:
	poetry run pre-commit uninstall && poetry run pre-commit install

.PHONY: lint
lint:
	poetry run pre-commit run --all-files


.PHONY: coverage
coverage:
	poetry run pytest --cov ./mermaid
