
# variables
POETRY_RUN		:= poetry run
PRE_COMMIT_CMD		:= $(POETRY_RUN) pre-commit

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

.PHONY: install/pre-commit
install/pre-commit:
	$(PRE_COMMIT_CMD) uninstall && $(PRE_COMMIT_CMD) install

.PHONY: lint
lint:
	$(PRE_COMMIT_CMD) run --all-files


.PHONY: coverage
coverage:
	$(POETRY_RUN) pytest --cov ./mermaid --cov-report=xml

mermaid.ink/up:
	docker run -p 3000:3000 -d --cap-add=SYS_ADMIN ghcr.io/jihchi/mermaid.ink

mermaid.ink/down:
	docker stop $(shell docker ps -q --filter ancestor=ghcr.io/jihchi/mermaid.ink)

.PHONY: bumpversion
bumpversion:
	$(eval name=$(filter-out $@,$(MAKECMDGOALS)))
	$(POETRY_RUN) bumpver update --$(name)
%:
	@:

.PHONY: help
help:
	@echo "run 'make <target>' where <target> is one of the following:"
	@echo ""
	@echo "  install           		install dependencies"
	@echo "  update            		update dependencies"
	@echo "  build             		build package"
	@echo "  publish           		publish package"
	@echo ""
	@echo "  test              		run tests"
	@echo "  install/pre-commit 		install pre-commit hooks"
	@echo "  lint              		run linters"
	@echo "  coverage          		run tests with coverage"
	@echo ""
	@echo "  bumpversion       		bump version"
	@echo "  help              		show this help message"
	@echo ""
	@echo "  mermaid.ink/up    		start mermaid.ink Local server"
	@echo "  mermaid.ink/down  		stop mermaid.ink local server"
