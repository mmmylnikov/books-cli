'''
This module provides the Book class.
'''

from dataclasses import dataclass, fields
from enum import Enum


class BookStatus(Enum):
    AVAILABLE = "available"
    ISSUED = "issued"

    def __str__(self) -> str:
        return self.value

    def __repr__(self) -> str:
        return self.value


@dataclass
class Book:
    id: int | None
    title: str
    author: str
    year: int
    status: BookStatus = BookStatus.AVAILABLE

    def __post_init__(self) -> None:
        for field_name in ['title', 'author']:
            attr_value = getattr(self, field_name)
            attr_value = attr_value.strip()
            attr_value = attr_value.replace("\n", " ")
            setattr(self, field_name, attr_value)

    def to_dict(self) -> dict:
        return {
            'id': self.id,
            'title': self.title,
            'author': self.author,
            'year': self.year,
            'status': self.status.value
        }

    @classmethod
    def from_dict(cls: type, data: dict) -> "Book":
        return cls(
            data["id"],
            data["title"],
            data["author"],
            data["year"],
            BookStatus(data["status"]),
        )

    @classmethod
    def get_fields(cls: type) -> list[str]:
        return [field.name for field in fields(cls)]

    @staticmethod
    def print_list_books_as_table(books: list["Book"]) -> str:
        output = ""
        output += (
            "{:>4} {:<25} {:<25} {:>4} {:<10}".format(*Book.get_fields())
        ) + "\n"
        output += ("-" * 79) + "\n"

        for book in books:
            output += (
                "{:>4} {:<25} {:<25} {:>4} {:<10}".format(
                    *book.to_dict().values()
                ) + "\n"
            )
        print(output)
        return output
