
SHELL := /bin/bash

APP_NAME = python_devops
PORT = 5000

default: help

init:
	python3 -m venv .venv && \
	source .venv/bin/activate && \
	pip install -r requirements.txt

run:
	source .venv/bin/activate && python3 health-calculator-service/app.py

build:
	docker build -t ${APP_NAME} .

test:
	source .venv/bin/activate && python3 health-calculator-service/test-utils.py

test-api:
	source .venv/bin/activate && python3 health-calculator-service/test-api.py

run-container:
	docker run -d --name ${APP_NAME} -p ${PORT}:${PORT} ${APP_NAME}

all: init build run-container test test-api

help:
	@echo "Availables commands"