FROM apache/airflow:2.5.3-python3.10
USER root
RUN apt-get update \
  && apt-get install -y --no-install-recommends \
    openjdk-11-jdk build-essential libopenmpi-dev openssh-server openssh-client libsasl2-dev \
  && apt-get autoremove -yqq --purge \
  && apt-get clean \
  && rm -rf /var/lib/apt/lists/*

USER airflow
COPY ./requirements.txt requirements.txt
RUN /usr/local/bin/python3 -m pip install --upgrade pip
RUN pip3 install --no-cache-dir "apache-airflow==${AIRFLOW_VERSION}" -r requirements.txt
COPY ./airflow_docker.cfg airflow.cfg