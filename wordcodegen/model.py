import enum
import pathlib
from dataclasses import dataclass
from typing import NamedTuple


class Language(NamedTuple):
    markdown_format: str
    comment_line_prefix: str


class ProgrammingLanguages(enum.Enum):
    PYTHON = Language(markdown_format="python", comment_line_prefix="# ")
    GO = Language(markdown_format="go", comment_line_prefix="// ")
    C = Language(markdown_format="c", comment_line_prefix="// ")
    CPP = Language(markdown_format="cpp", comment_line_prefix="// ")

    @classmethod
    def from_extension(cls, file_extension: str) -> Language:
        match file_extension:
            case ".py":
                return cls.PYTHON.value
            case ".go":
                return cls.GO.value
            case ".c":
                return cls.C.value
            case ".cpp" | ".cc" | ".cxx" | ".h":
                return cls.CPP.value
            case _:
                raise ValueError(f"Unknown extension {file_extension}")


@dataclass
class SourceCode:
    path: pathlib.Path
    code: str
    language: Language

    def to_markdown(self) -> str:
        return f"""```{self.language.markdown_format}\n{self.language.comment_line_prefix}{self.path.absolute()}\n{self.code}\n```\n"""
