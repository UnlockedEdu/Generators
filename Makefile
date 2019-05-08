clean:
	rm -rf dist/
	rm -rf build/
	rm -rf __pycache__/
	rm -rf *.egg-info
	rm -rf logs/

build-py:
	pipenv run python3 setup.py bdist_wheel

build-docker:
	docker build -t unlockededu/docs-gen .

build: build-py build-docker

test: static-analysis test-python

static-analysis:
	pipenv run pylint code_generators

test-python:
	pipenv lock -r > requirements.txt
	pipenv lock -r --dev >> requirements.txt
	pipenv run tox
	rm -f requirements.txt

lock:
	pipenv lock

prepare-agent:
	@ln -sfn /var/tmp/.local /home/build/.local
	@ln -sfn /var/tmp/.cache /home/build/.cache
	pipenv install --dev

#####
# Optional Targets
#####

run:
	@echo 'To test this go to localhost:8080'
	docker run --rm -it --name docs-gen \
		-p 8080:5000 \
		-e APP_LOG_LEVEL="DEBUG" \
		unlockededu/docs-gen

start:
	@echo 'To test this go to localhost:8080'
	docker run --rm -d --name docs-gen \
		-p 8080:5000 \
		-e APP_LOG_LEVEL="DEBUG" \
		unlockededu/docs-gen


stop:
	docker kill unlockededu/docs-gen

bash:
	docker run -it $(DOCKER_REGISTRY)/$(GROUP)/$(ARTIFACT):$(VERSION) /bin/bash
