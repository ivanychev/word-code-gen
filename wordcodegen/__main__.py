import pathlib

import click

from wordcodegen.codeloader import load_code_from_notebook, load_code_from_source_files
from wordcodegen.convert import convert_to_word
from wordcodegen.finder import find_sources_in_folder


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
def convert_ipynb(path: str, output_path: str, reference_docx_path: str | None):
    reference_docx_path = (
        pathlib.Path(reference_docx_path) if reference_docx_path else None
    )
    path = pathlib.Path(path)
    code = load_code_from_notebook(path)
    convert_to_word(
        [code], pathlib.Path(output_path), reference_docx_path=reference_docx_path
    )


# python -m wordcodegen convert-source-files \
# --folder=/Users/iv/Code/advent-of-code-2022/advent/monkey_21_12 \
# --folder=/Users/iv/Code/advent-of-code-2022/advent/monkey_map_22 \
# --folder=/Users/iv/Code/advent-of-code-2022/advent/unstable_diffusion_23_12 \
# --folder=/Users/iv/Code/advent-of-code-2022/advent/blizzard_24_12 \
# --folder=/Users/iv/Code/advent-of-code-2022/advent/air_25_12 \
# --folder=/Users/iv/Code/adventOfCode/src
@cli.command()
@click.option(
    "--path",
    "-i",
    multiple=True,
    help="Path to the converted source file(s)",
    type=str,
)
@click.option(
    "--folder",
    "-f",
    multiple=True,
    help="Path to the folder, containing the source files",
    type=str,
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
@click.option(
    "--file-extensions",
    help="File extensions to process.",
    default=["py", "go", "c", "cc", "cpp", "cxx"],
    type=list[str],
)
def convert_source_files(
    path: list[str],
    folder: list[str],
    output_path: str,
    reference_docx_path: str | None,
    file_extensions: list[str],
):
    reference_docx_path = (
        pathlib.Path(reference_docx_path) if reference_docx_path else None
    )
    paths = None
    if path:
        paths = [pathlib.Path(p) for p in path]
    elif folder:
        paths = [
            p
            for f in folder
            for p in find_sources_in_folder(pathlib.Path(f), file_extensions)
        ]
    code = load_code_from_source_files(paths)
    convert_to_word(
        code, pathlib.Path(output_path), reference_docx_path=reference_docx_path
    )


if __name__ == "__main__":
    cli()
