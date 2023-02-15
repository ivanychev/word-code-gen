FROM python:3.11-slim

SHELL ["/bin/bash", "-o", "pipefail", "-c"]


ENV DEBIAN_FRONTEND=noninteractive
ENV POETRY_HOME=/opt/poetry
ENV POETRY_VIRTUALENVS_IN_PROJECT=true
ENV PATH="$POETRY_HOME/bin:$PATH"
ENV REFERENCE_ENV_PATH="/opt/reference.docx"

RUN apt-get update && \
    apt-get install pandoc -y && \
    apt-get clean && rm -rf /var/lib/apt/lists/* /tmp/* /var/tmp/*

ADD poetry.lock pyproject.toml /opt/

WORKDIR /opt

RUN python -c 'import urllib.request, sys; print(urllib.request.urlopen(f"{sys.argv[1]}").read().decode("utf8"))' https://install.python-poetry.org  | \
    POETRY_VERSION=1.2.0 python3 - && \
    poetry config virtualenvs.create false && \
    poetry install --no-root --only main && \
    rm -rf ~/.cache/pypoetry/{cache,artifacts} && \
    rm -rf /opt/poetry

ADD wordcodegen /opt/wordcodegen
ADD reference.docx /opt/reference.docx
