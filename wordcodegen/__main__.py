import pathlib

import click
import pandoc

from wordcodegen.codeloader import load_code_from_notebook, load_code_from_source_files
from wordcodegen.convert import convert_to_word


@click.group()
def cli():
    pass


@cli.command()
@click.option(
    "--path", "-i", help="Path to the converted notebook", type=str, required=True
)
@click.option(
    "--output-path",
    "-o",
    help="Path to the output docx file.",
    default="converted.docx",
)
@click.option(
    "--reference-docx-path",
    "-o",
    help="Path to the reference docx file that is used for styling output doc.",
    default=None,
    type=str,
)
def convert_ipynb(path: str, output_path: str,
                  reference_docx_path: str | None):
    reference_docx_path = pathlib.Path(reference_docx_path) if reference_docx_path else None
    path = pathlib.Path(path)
    code = load_code_from_notebook(path)
    convert_to_word(code, pathlib.Path(output_path),
                    reference_docx_path=reference_docx_path)


@cli.command()
@click.option(
    "--path",
    "-i",
    multiple=True,
    help="Path to the converted source file(s)",
    type=str,
    required=True,
)
@click.option(
    "--output-path",
    "-o",
    help="Path to the output docx file.",
    default="converted.docx",
    nargs=1,
)
@click.option(
    "--reference-docx-path",
    "-o",
    help="Path to the reference docx file that is used for styling output doc.",
    default=None,
    type=str,
)
def convert_source_files(path: list[str], output_path: str,
                         reference_docx_path: str | None):
    reference_docx_path = pathlib.Path(reference_docx_path) if reference_docx_path else None
    path = [pathlib.Path(p) for p in path]
    code = load_code_from_source_files(path)
    convert_to_word(code, pathlib.Path(output_path),
                    reference_docx_path=reference_docx_path)


if __name__ == "__main__":
    cli()
