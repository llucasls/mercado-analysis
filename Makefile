USER_SHELL = /bin/bash
VENV = .venv
USER_VIRTUAL_ENVIRONMENT = $(PWD)/$(VENV)

PYTHON = python
PIP = $(PYTHON) -m pip

activate: | $(USER_VIRTUAL_ENVIRONMENT)
	if test -z "$${VIRTUAL_ENV}"; then \
		. $(USER_VIRTUAL_ENVIRONMENT)/bin/activate && $(USER_SHELL); \
	fi

install: $(USER_VIRTUAL_ENVIRONMENT)

$(USER_VIRTUAL_ENVIRONMENT): requirements.txt
	if test ! -d $(USER_VIRTUAL_ENVIRONMENT); then \
		$(PYTHON) -m venv $(USER_VIRTUAL_ENVIRONMENT); \
	fi
	. $(USER_VIRTUAL_ENVIRONMENT)/bin/activate && $(PIP) install -r requirements.txt
	touch $(USER_VIRTUAL_ENVIRONMENT)

dev: | $(USER_VIRTUAL_ENVIRONMENT)
	$(USER_VIRTUAL_ENVIRONMENT)/bin/flask --debug --app src.app run

.PHONY: install activate dev
