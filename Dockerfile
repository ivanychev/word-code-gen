FROM python:3.11

SHELL ["/bin/bash", "-o", "pipefail", "-c"]


ENV DEBIAN_FRONTEND=noninteractive
ENV POETRY_HOME=/opt/poetry
ENV POETRY_VIRTUALENVS_IN_PROJECT=true
ENV PATH="$POETRY_HOME/bin:$PATH"
ENV REFERENCE_ENV_PATH="/opt/reference.docx"

RUN apt-get update && \
    apt-get install pandoc curl -y && \
    apt-get clean && rm -rf /var/lib/apt/lists/* /tmp/* /var/tmp/*

RUN curl -sSL https://install.python-poetry.org  | POETRY_VERSION=1.2.0 python3 -

ADD poetry.lock pyproject.toml /opt/

WORKDIR /opt

RUN poetry config virtualenvs.create false && \
    poetry install --no-root --only main && \
    rm -rf ~/.cache/pypoetry/{cache,artifacts} && \
    rm -rf /opt/poetry

ADD wordcodegen /opt/wordcodegen
ADD reference.docx /opt/reference.docx
