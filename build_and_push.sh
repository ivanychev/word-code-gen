#!/usr/bin/env bash

set -euxo pipefail

docker_image="ivanychev/word-code-gen"
docker_tag="$(tomlq -r ".tool.poetry.version" pyproject.toml)"

docker buildx build \
      --platform linux/arm64/v8,linux/amd64 \
      -f Dockerfile \
      -t "${docker_image}:${docker_tag}" \
      --push \
      .
