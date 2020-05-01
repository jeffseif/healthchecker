.DELETE_ON_ERROR:

LOCKFILE = .already.running.lock
PYTHON = $(shell which python3)
VENV = venv/

HOST = 0.0.0.0
PORT ?= 5000
WSGI = wsgi.py


.PHONY: daemon
daemon: $(LOCKFILE)

$(LOCKFILE): $(VENV) $(WSGI) | already_running
	@touch $@
	@FLASK_ENV=development FLASK_RUN_HOST=$(HOST) FLASK_RUN_PORT=$(PORT) $</bin/flask run
	@rm -f $@

.PHONY: already_running
already_running:
	@test ! -e $(LOCKFILE) || exit 0

$(VENV): requirements-minimal.txt
	@virtualenv \
		--python=$(PYTHON) \
		$@
	@$@/bin/pip install \
		--requirement $<
	@$@/bin/pip install \
		--upgrade pip
	@touch $@

clean:
	@rm -rf $(VENV)
	@find . -name '*.pyc' -delete
	@find . -name '__pycache__' -type d -delete
