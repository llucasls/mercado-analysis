PYTHON = python
PIP = $(PYTHON) -m pip
FLASK = $(PYTHON) -m flask

dev:
	FLASK_APP=src/app.py FLASK_ENV=development $(FLASK) run

install:
	$(PIP) install -r requirements.txt

.PHONY: install dev
