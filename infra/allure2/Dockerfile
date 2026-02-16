FROM python:3.12-slim

RUN apt-get update && apt-get install -y \
    wget \
    curl \
    build-essential \
    docker.io \
    && curl -fsSL https://deb.nodesource.com/setup_20.x | bash - \
    && apt-get install -y nodejs \
    && rm -rf /var/lib/apt/lists/*

RUN wget https://github.com/allure-framework/allure2/releases/download/2.29.0/allure-2.29.0.tgz \
    && tar -xf allure-2.29.0.tgz -C /opt/ \
    && ln -s /opt/allure-2.29.0/bin/allure /usr/bin/allure \
    && rm allure-2.29.0.tgz

WORKDIR /app
COPY requirements.txt .
RUN pip install --no-cache-dir -r requirements.txt


EXPOSE 8080
