FROM python:3.12-slim

RUN apt-get update && apt-get install -y \
    wget \
    curl \
    build-essential \
    docker.io \
    && curl -fsSL https://deb.nodesource.com/setup_20.x | bash - \
    && apt-get install -y nodejs \
    && rm -rf /var/lib/apt/lists/*

RUN npm install -g allure@latest

WORKDIR /app
COPY requirements.txt .
RUN pip install --no-cache-dir -r requirements.txt


EXPOSE 8081
