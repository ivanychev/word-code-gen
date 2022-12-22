import pathlib


def find_sources_in_folder(
    path: pathlib.Path, file_extension: str = "py"
) -> list[pathlib.Path]:
    return list(path.rglob(f"**/*.{file_extension}"))
