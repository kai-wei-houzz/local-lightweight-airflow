PACKAGES := "dags"

.PHONY: build
build:
	docker build . -f Dockerfile --tag airflow:dev

.PHONY: version
version:
	docker run --rm --name testairflow airflow:dev version

.PHONY: up
up:
	docker compose up -d 

.PONHY: down
down:
	docker compose down