# Makefile to build findbiz

PATH := $(PWD)/scripts:$(PATH)
APP_NAME = findbiz
APP_VERSION ?= latest
VENV_NM ?=
VENV_DIR := .venv
GEM_URL = --source http://rubygems.org
FPM_BUILD_DEPS = ruby-devel ruby-irb ruby-rdoc ruby-ri gcc make rpm-build rubygems
ANSIBLE_EXTRA_VARS ?= ansible_port=2222

$(VENV_DIR):
	python3 -m venv --clear $(VENV_DIR)

.PHONY: build
build: $(VENV_DIR)
	. $(VENV_DIR)/bin/activate; \
	pip install --upgrade --verbose setuptools && \
	pip install --upgrade --verbose wheel && \
	pip install --upgrade --verbose pip && \
	pip install --verbose -r requirements.txt

.PHONY: clean
clean:
	rm -vfr $(VENV_DIR)
