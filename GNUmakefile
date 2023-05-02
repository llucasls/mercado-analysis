USER_SHELL = /bin/bash

VENV = $(CURDIR)/.venv

PYTHON = python3
PIP = $(PYTHON) -m pip

activate: | $(VENV)
	if test -z "$${VIRTUAL_ENV}"; then \
		. $(VENV)/bin/activate && $(USER_SHELL); \
	fi

install: $(VENV)

$(VENV): requirements.txt
	if test ! -d $(VENV); then \
		$(PYTHON) -m venv $(VENV); \
	fi
	. $(VENV)/bin/activate && $(PIP) install -r requirements.txt
	touch $(VENV)

dev: | $(VENV)
	$(VENV)/bin/flask --debug --app src.app run

.PHONY: install activate dev
