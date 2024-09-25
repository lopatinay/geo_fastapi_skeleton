.PHONY: compile-versions
compile-versions:
	pip-compile -v --output-file requirements/requirements.txt requirements/requirements.in
	pip-compile -v --output-file requirements/dev_requirements.txt requirements/requirements.txt requirements/dev_requirements.in


install:
	pip install -r requirements/dev_requirements.txt


migrate:
	alembic upgrade head

rollback:
	alembic downgrade -1

dev:
	pip install -r requirements/dev_requirements.txt

flake:
	flake8 --show-source --statistics


test:
	pytest tests



check:
	$(MAKE) flake
	$(MAKE) test
