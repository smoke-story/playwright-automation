FROM python:3.13.9-bookworm

ENV PYTHONUNBUFFERED=1

# Set environment variables for Allure
ENV ALLURE_VERSION=2.35.0

# Installing allure-commandline
RUN apt-get update \
    && apt-get install -y --no-install-recommends openjdk-17-jre-headless curl \
    && curl -o allure-${ALLURE_VERSION}.tgz -Ls https://repo.maven.apache.org/maven2/io/qameta/allure/allure-commandline/${ALLURE_VERSION}/allure-commandline-${ALLURE_VERSION}.tgz \
    && tar -zxvf allure-${ALLURE_VERSION}.tgz -C /opt/ \
    && ln -s /opt/allure-${ALLURE_VERSION}/bin/allure /usr/bin/allure \
    && rm allure-${ALLURE_VERSION}.tgz \
    && apt-get clean && rm -rf /var/lib/apt/lists/*
    && ls -la /opt/

WORKDIR /usr/workspace

COPY ./requirements.txt /usr/workspace

RUN pip install --no-cache-dir -r requirements.txt \
    && playwright install --with-deps --only-shell \
    && ls -la /usr/local/lib
    