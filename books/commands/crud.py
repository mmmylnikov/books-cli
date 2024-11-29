'''
This module provides the Add, Update, Remove, Clear and List commands.
'''

from argparse import Namespace, _SubParsersAction

from books.books import Book, BookStatus
from books.commands.commands import Command
from books.database import BookDatabase


class Add(Command):
    def add_subparsers(self, subparsers: _SubParsersAction) -> None:
        add_parser = subparsers.add_parser('add', help='Add a new book')
        add_parser.add_argument('title', type=str, help='Title of the book')
        add_parser.add_argument('author', type=str, help='Author of the book')
        add_parser.add_argument('year', type=int, help='Year of publication')
        self.parser = add_parser

    def __call__(self, db: BookDatabase, args: Namespace) -> None:
        book = Book(
            id=None, title=args.title, author=args.author, year=args.year
        )
        db.add_book(book)
        print(f"{book} added successfully.")


class Update(Command):
    def add_subparsers(self, subparsers: _SubParsersAction) -> None:
        update_parser = subparsers.add_parser(
            "update", help="Update the status of a book"
        )
        update_parser.add_argument("id", type=int, help="ID of the book")
        update_parser.add_argument(
            "status",
            choices=[member.value for member in BookStatus],
            help="New status of the book",
        )
        self.parser = update_parser

    def __call__(self, db: BookDatabase, args: Namespace) -> None:
        book = db.update_book_status(args.id, args.status)
        if not book:
            print(f"Book with ID {args.id} not found.")
        else:
            print(f"{book} status updated successfully.")


class Remove(Command):
    def add_subparsers(self, subparsers: _SubParsersAction) -> None:
        remove_parser = subparsers.add_parser(
            "remove", help="Remove a book by ID"
        )
        remove_parser.add_argument(
            "id", type=int, help="ID of the book to remove"
        )
        self.parser = remove_parser

    def __call__(self, db: BookDatabase, args: Namespace) -> None:
        book = db.remove_book(args.id)
        if not book:
            print(f"Book with ID {args.id} not found.")
        else:
            print(f"{book} removed successfully.")


class Clear(Command):
    def add_subparsers(self, subparsers: _SubParsersAction) -> None:
        clear_parser = subparsers.add_parser(
            'clear', help='Clear all books')
        self.parser = clear_parser

    def __call__(self, db: BookDatabase, args: Namespace) -> None:
        answer = input("Are you sure? [y/N]: ")
        if answer.lower() != "y":
            print("Operation cancelled.")
            return
        db.clear_books()
        print("All books cleared.")


class List(Command):
    def add_subparsers(self, subparsers: _SubParsersAction) -> None:
        list_parser = subparsers.add_parser(
            'list', help='List all books')
        self.parser = list_parser

    def __call__(self, db: BookDatabase, args: Namespace) -> None:
        Book.print_list_books_as_table(list(db.get_books().values()))
