PACKAGES := "dags"

.PHONY: build
build:
	docker build . -f Dockerfile --tag airflow:dbt

.PHONY: version
version:
	docker run --rm --name testairflow airflow:dbt version

.PHONY: up
up:
	docker compose up -d 

.PONHY: down
down:
	docker compose down