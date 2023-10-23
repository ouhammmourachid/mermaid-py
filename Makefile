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