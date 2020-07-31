PY=/usr/bin/env python3

.PHONY: all test build

all:

test:
	cd regress && $(MAKE)

build:
	$(PY) setup.py sdist bdist_wheel
