FROM python:3.12-slim

RUN apt-get update && apt-get install -y \
    openjdk-21-jre-headless \
    wget \
    tar \
    build-essential \
    docker.io \
    && rm -rf /var/lib/apt/lists/*

ENV JAVA_HOME=/usr/lib/jvm/java-21-openjdk-amd64
ENV PATH="$JAVA_HOME/bin:$PATH"

RUN wget https://github.com/allure-framework/allure2/releases/download/2.29.0/allure-2.29.0.tgz \
    && tar -xf allure-2.29.0.tgz -C /opt/ \
    && ln -s /opt/allure-2.29.0/bin/allure /usr/bin/allure \
    && rm allure-2.29.0.tgz

WORKDIR /app

RUN pip install --no-cache-dir \
    pytest \
    allure-pytest \
    pytest-html \
    requests \
    pyyaml \
    cryptography

EXPOSE 8080