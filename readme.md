# Airflow dev environment with Docker
## Prerequisite 
- python 3.10
- Docker 

## Getting started
1. Initiate a virtual env \
    ``` bash
    # create an venv in current dir
    python -m venv .venv 
    # Activate the venv
    source .venv/bin/activate
    ```
2. Build Docker \
    `make build`
3. Start the service \
    `make up`
4. login to UI in [`localhost:8080`](http://localhost:8080)

## Note
- Specify airflow, python version in docker file
- `apt-get update/install {required packages}` if pip install failed
- To make it lightweight, 
    - Change `AIRFLOW__CORE__EXECUTOR` to `LocalExecutor` \
    - Comment out `celery`, `redis`, `flower` related settings
- Specify DAG file path in docker-compose file 
    ```yaml
    volumes:
     - ./dags:/opt/airflow/dags
     ```
- Load examples setting in docker-compose file \
    ```yaml
    AIRFLOW__CORE__LOAD_EXAMPLES: 'false'
    ```
        
## TO-DO
- Load connections, variables into 