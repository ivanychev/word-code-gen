import json
import pathlib
from collections.abc import Iterable


def load_code_from_notebook(notebook_path: pathlib.Path) -> str:
    with notebook_path.open() as f:
        notebook = json.load(f)

    code_cells = [cell for cell in notebook["cells"] if cell["cell_type"] == "code"]

    return "\n".join(line for cell in code_cells for line in cell["source"])


def load_code_from_source_files(paths: list[pathlib.Path]) -> str:
    return "\n".join(_load_code_from_source_files_gen(paths))


def _load_code_from_source_files_gen(paths: list[pathlib.Path]) -> Iterable[str]:
    for p in paths:
        with p.open() as f:
            for line in f:
                yield line.strip("\n")
