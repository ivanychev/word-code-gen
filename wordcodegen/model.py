import enum
import pathlib
from dataclasses import dataclass
from typing import NamedTuple


class Language(NamedTuple):
    markdown_format: str
    comment_line_prefix: str
    comment_line_suffix: str = ""


class ProgrammingLanguages(enum.Enum):
    PYTHON = Language(markdown_format="python", comment_line_prefix="# ")
    GO = Language(markdown_format="go", comment_line_prefix="// ")
    YAML = Language(markdown_format="yaml", comment_line_prefix="# ")
    HTML = Language(markdown_format="html", comment_line_prefix="<!--", comment_line_suffix="-->")
    RUST = Language(markdown_format="rust", comment_line_prefix="// ")
    C = Language(markdown_format="c", comment_line_prefix="// ")
    CPP = Language(markdown_format="cpp", comment_line_prefix="// ")
    ASM = Language(markdown_format="asm", comment_line_prefix="// ")

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
            case ".asm":
                return cls.ASM.value
            case ".yaml" | ".yml":
                return cls.YAML.value
            case ".html":
                return cls.HTML.value
            case ".rs":
                return cls.RUST.value
            case _:
                raise ValueError(f"Unknown extension {file_extension}")


@dataclass
class SourceCode:
    path: pathlib.Path
    code: str
    language: Language

    def to_markdown(self) -> str:
        return f"""```{self.language.markdown_format}\n{self.language.comment_line_prefix}{self.path.absolute()}{self.language.comment_line_suffix}\n{self.code}\n```\n"""
