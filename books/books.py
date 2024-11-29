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
    def print_list_books_as_table(books: list["Book"]) -> None:
        print("{:>4} {:<25} {:<25} {:>4} {:<10}".format(*Book.get_fields()))
        print("-" * 79)

        for book in books:
            print(
                "{:>4} {:<25} {:<25} {:>4} {:<10}".format(
                    *book.to_dict().values()
                )
            )
