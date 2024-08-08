
# variables
POETRY_RUN		= poetry run
PRE_COMMIT_CMD	= $(POETRY_RUN) pre-commit

.PHONY: install
install:
	poetry install

.PHONY: update
update:
	poetry update

.PHONY: build
build:
	poetry build

.PHONY: publish
publish:
	poetry publish

.PHONY: test
test:
	$(POETRY_RUN) pytest

.PHONY: install-pre-commit
install-pre-commit:
	$(PRE_COMMIT_CMD) uninstall && $$(PRE_COMMIT_CMD) install

.PHONY: lint
lint:
	$(PRE_COMMIT_CMD) run --all-files


.PHONY: coverage
coverage:
	$(POETRY_RUN) pytest --cov ./mermaid --cov-report=xml

.PHONY: bumpversion
bumpversion:
	$(eval name=$(filter-out $@,$(MAKECMDGOALS)))
	$(POETRY_RUN) bumpver update --$(name)
%:
	@:
