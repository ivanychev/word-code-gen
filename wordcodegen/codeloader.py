import io
import itertools
import json
import pathlib
from collections.abc import Iterable
from operator import attrgetter

from loguru import logger

from wordcodegen.model import ProgrammingLanguages, SourceCode


def load_code_from_notebook(notebook_path: pathlib.Path) -> SourceCode:
    with notebook_path.open() as f:
        notebook = json.load(f)

    code_cells = [cell for cell in notebook["cells"] if cell["cell_type"] == "code"]

    python_code = "\n".join(line for cell in code_cells for line in cell["source"])
    return SourceCode(
        code=python_code, language=ProgrammingLanguages.PYTHON.value, path=notebook_path
    )


def load_code_from_source_files(paths: list[pathlib.Path]) -> list[SourceCode]:
    return list(_load_code_from_source_files_gen(paths))


def _load_code_from_source_files_gen(paths: list[pathlib.Path]) -> Iterable[SourceCode]:
    for suffix, files in itertools.groupby(paths, key=attrgetter("suffix")):
        lang = ProgrammingLanguages.from_extension(suffix)
        buffer = io.StringIO()
        for p in files:
            logger.info("Processing {}...", p)
            with p.open() as f:
                buffer.write(f.read())
        yield SourceCode(code=buffer.getvalue(), language=lang, path=p)
