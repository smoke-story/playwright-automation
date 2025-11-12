# First stage
FROM python:3.10.19-slim-bookworm AS builder

ENV PYTHONUNBUFFERED=1

ENV ALLURE_VERSION=2.35.0

RUN apt-get update \
    && apt-get install -y --no-install-recommends openjdk-17-jre-headless curl \
    && curl -o allure-${ALLURE_VERSION}.tgz -Ls https://repo.maven.apache.org/maven2/io/qameta/allure/allure-commandline/${ALLURE_VERSION}/allure-commandline-${ALLURE_VERSION}.tgz \
    && tar -zxvf allure-${ALLURE_VERSION}.tgz -C /opt/ \
    && ln -s /opt/allure-${ALLURE_VERSION}/bin/allure /usr/bin/allure \
    && rm allure-${ALLURE_VERSION}.tgz \
    && apt-get clean \
    && rm -rf /var/lib/apt/lists/* \
    && rm -rf /tmp/* \
    && rm -rf /var/tmp/*

WORKDIR /usr/workspace

COPY ./requirements.txt /usr/workspace

RUN pip install --no-cache-dir -r requirements.txt

# Second stage
FROM python:3.10.19-slim-bookworm AS main

ENV PYTHONUNBUFFERED=1

ENV ALLURE_VERSION=2.35.0

COPY --from=builder /usr/local/bin/* /usr/local/bin

COPY --from=builder /usr/local/lib/python3.10/site-packages /usr/local/lib/python3.10/site-packages

COPY --from=builder /usr/lib/jvm/java-17-openjdk-amd64 /usr/lib/jvm/java-17-openjdk-amd64

COPY --from=builder /opt/allure-${ALLURE_VERSION} /opt/allure-${ALLURE_VERSION}

RUN ln -s usr/lib/jvm/java-17-openjdk-amd64/bin/java /usr/bin/java \
    && ln -s /opt/allure-${ALLURE_VERSION}/bin/allure /usr/bin/allure

RUN playwright install --with-deps --only-shell \
    && apt-get clean \
    && rm -rf /var/lib/apt/lists/* \
    && rm -rf /tmp/* \
    && rm -rf /var/tmp/*
