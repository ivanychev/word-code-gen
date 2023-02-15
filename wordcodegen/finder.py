import pathlib


def find_sources_in_folder(
    path: pathlib.Path, file_extensions: list[str]
) -> list[pathlib.Path]:

    paths = []
    for ext in file_extensions:
        if not ext.startswith("."):
            ext = "." + ext
        paths.extend(path.rglob(f"**/*{ext}"))
    return paths
