import pathlib
import re
from typing import Sequence

from loguru import logger

# Regex to filter out ("/.venv/", "/.git/", "/__pycache__/", "venv", "node_modules"),
EXCLUDE_PATTERN = re.compile(r"^(?!.*(/\.venv/|/.git/|/venv/|/__pycache__/|venv|node_modules)).*$")

def find_sources_in_folder(
    path: pathlib.Path, file_extensions: list[str]
) -> list[pathlib.Path]:

    paths = []
    for ext in file_extensions:
        if not ext.startswith("."):
            ext = "." + ext
        for f in path.rglob(f"**/*{ext}"):
            included = bool(EXCLUDE_PATTERN.match(str(f.absolute())))
            if included:
                paths.append(f)
                logger.info("Found source file: {}", f)
            else:
                logger.debug("Skipping file: {}", f)
        # paths.extend(path.rglob(f"**/*{ext}"))
    return paths
