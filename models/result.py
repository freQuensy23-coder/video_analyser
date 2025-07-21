import dataclasses
from typing import Literal


@dataclasses.dataclass
class VideoParseResult:
    short_summary: str
    company_name: str
    tags: list[str]
    technical_stack: list[str]
    questions: list[str]

@dataclasses.dataclass
class Question:
    question: str
    field: Literal['sql', 'math', 'ml', 'ds', 'nlp', 'cv', 'python', 'general']
