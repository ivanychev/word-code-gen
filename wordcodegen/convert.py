import os
import pathlib
import subprocess
import tempfile

from wordcodegen.decorate import convert_code_to_markdown

REFERENCE_ENV_PATH = 'REFERENCE_ENV_PATH'


def get_reference_docx_path() -> pathlib.Path:
    if REFERENCE_ENV_PATH in os.environ:
        path = pathlib.Path(os.environ[REFERENCE_ENV_PATH]).absolute()
        assert path.exists()
        return path

    cwd_reference = pathlib.Path(os.getcwd()) / 'reference.docx'
    if cwd_reference.exists():
        return cwd_reference.absolute()

    raise RuntimeError("Reference docx not found")


def convert_to_word(source_code: str, output_file_path: pathlib.Path,
                    reference_docx_path: pathlib.Path | None):
    reference_docx_path = reference_docx_path or get_reference_docx_path()
    output_file_path = output_file_path.absolute()
    with tempfile.TemporaryDirectory() as tmpdir:
        dir_path = pathlib.Path(tmpdir)

        md_file_path = dir_path / "code.md"
        with md_file_path.open("w") as f:
            f.write(convert_code_to_markdown(source_code))

        subprocess.call(
            ["pandoc", str(md_file_path.absolute()), "-s", "-o", str(output_file_path),
             "--reference-doc",
             str(reference_docx_path.absolute())],
        )
