VENV_NAME?=venv
VENV_ACTIVATE=. $(VENV_NAME)/bin/activate
PYTHON=${VENV_NAME}/bin/python3

dev:
	python3 -m pip install virtualenv
	make venv

venv: $(VENV_NAME)/bin/activate
$(VENV_NAME)/bin/activate: requirements.txt
	test -d $(VENV_NAME) || virtualenv -p python3 $(VENV_NAME)
	${PYTHON} -m pip install -U pip
	${PYTHON} -m pip install -r requirements.txt
	touch $(VENV_NAME)/bin/activate

test:
	tox

clean: clean-build clean-test clean-venv clean-pyc

clean-build:
	rm -rf build/
	rm -rf .eggs/
	find . -name '*.egg-info' -exec rm -f {} +
	find . -name '*.egg' -exec rm -f {} +

clean-test:
	rm -rf .tox/

clean-venv:
	rm -rf venv

clean-pyc:
	find . -name '*.pyc' -exec rm -f {} +
	find . -name '*.pyo' -exec rm -f {} +
	find . -name '*~' -exec rm -f {} +
	find . -name '__pycache__' -exec rm -f {} +
