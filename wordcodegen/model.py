import enum
from dataclasses import dataclass
from typing import NamedTuple


class Language(NamedTuple):
    markdown_format: str


class ProgrammingLanguages(enum.Enum):
    PYTHON = Language(markdown_format="python")
    GO = Language(markdown_format="go")

    @classmethod
    def from_extension(cls, file_extension: str) -> Language:
        match file_extension:
            case ".py":
                return cls.PYTHON.value
            case ".go":
                return cls.GO.value
            case _:
                raise ValueError(f"Unknown extension {file_extension}")


@dataclass
class SourceCode:
    code: str
    language: Language

    def to_markdown(self) -> str:
        return f"""```{self.language.markdown_format}\n{self.code}\n```\n"""
