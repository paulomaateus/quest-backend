.PHONY: help venv run
.DEFAULT: help

VENV?=venv
PYTHON=$(VENV)/bin/python3
PIP=$(PYTHON) -m pip
INSTALLED=$(VENV)/installed
MODULE=serverquest

help:
	@echo "make venv: creates a new virtual enviroment."
	@echo ""
	@echo "make run: start the server. It runs the venv"
	@echo "          command to prepare the enviroment."

venv: $(VENV)/bin/activate
$(VENV)/bin/activate: requirements.txt
	test -d $(VENV) || python3 -m venv $(VENV)
	$(PIP) install --upgrade pip
	$(PIP) install --requirement requirements.txt
	touch $(VENV)/bin/activate

run: venv
	$(PYTHON) -m $(MODULE)