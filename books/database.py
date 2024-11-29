'''
This module provides the Books database functionality
'''

import json
import os

from books.books import Book, BookStatus


dir_path = os.path.dirname(os.path.realpath(__file__))


class BookDatabase:
    db_file: str
    books: dict[int, Book]
    next_id: int

    def __init__(
        self, db_file: str = os.path.join(dir_path, "books.json")
    ) -> None:
        self.db_file = db_file
        self.load()

    def get_next_id(self) -> int:
        if not self.books:
            return 1
        return max(book_id for book_id in self.books) + 1

    def books_to_dict(self) -> dict[int, dict]:
        return {
            book_id: book.to_dict() for book_id, book in self.books.items()
        }

    def get_books(self) -> dict[int, Book]:
        return self.books

    def load(self) -> None:
        if os.path.exists(self.db_file):
            with open(self.db_file, 'r') as f:
                self.books = {
                    int(book_id_str): Book.from_dict(book_raw)
                    for book_id_str, book_raw in json.load(f).items()
                }
        else:
            self.books = dict()
        self.next_id = self.get_next_id()

    def save(self) -> None:
        with open(self.db_file, 'w') as f:
            json.dump(self.books_to_dict(), f, indent=4, ensure_ascii=False)

    def add_book(self, book: Book) -> None:
        book.id = self.next_id
        self.books[book.id] = book
        self.next_id += 1
        self.save()

    def update_book_status(self, id: int, status: str) -> Book | None:
        if id not in self.books:
            return None
        self.books[id].status = BookStatus(status)
        self.save()
        return self.books[id]

    def remove_book(self, id: int) -> Book | None:
        if id not in self.books:
            return None
        book = self.books.pop(id)
        self.save()
        return book

    def clear_books(self) -> None:
        self.books = dict()
        self.save()

    def find_books(
        self,
        title: str | None = None,
        author: str | None = None,
        year: int | None = None,
    ) -> list[Book]:
        return [
            book
            for book in self.books.values()
            if all([
                title is None or title.lower() in book.title.lower(),
                author is None or author.lower() in book.author.lower(),
                year is None or book.year == year,
            ])
        ]
