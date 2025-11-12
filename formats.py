from dataclasses import dataclass, field


@dataclass
class Book:
    isbn: int  = 0
    title: str = ""
    authors: str = ""
    publisher: str = ""
    publish_year: int = 0
    pages: int = 0