# https://www.gnu.org/software/make/manual/html_node/One-Shell.html
# https://www.gnu.org/software/make/manual/html_node/Phony-Targets.html
.ONESHELL:
.PHONY: clean lint test run venv

BIN=./venv/bin
IMAGE_NAME=myfastapiimage
IMAGE_VERSION=1.0.0

venv: requirements.txt
	python3 -m venv ./venv
	$(BIN)/pip3 install -r requirements.txt

clean:
	rm -rf venv
	find . -type f -name *.pyc -delete
	find . -type d -name __pycache__ -exec rm -rf {} +
	find . -type d -name ".pytest_cache" -exec rm -rf {} +
	rm -rf .coverage
	rm -rf generated

lint: venv
	$(BIN)/black ./app/
	$(BIN)/black ./tests/
	$(BIN)/flake8 ./app/

test: lint
	rm -rf generated
	$(BIN)/coverage run -m pytest --cache-clear -v .
	$(BIN)/coverage report -m
	$(BIN)/coverage html -d generated/coverage
	$(BIN)/pdoc --html app -o generated/docstring

run: test
	$(BIN)/python3 -m app.main

docker-build: test
	docker build -t $(IMAGE_NAME):$(IMAGE_VERSION) .

docker-run:
	docker run --rm --name $(IMAGE_NAME) -p 8000:8000 $(IMAGE_NAME):$(IMAGE_VERSION)