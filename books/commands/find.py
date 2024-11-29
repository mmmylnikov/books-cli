'''
Find books by title, author or year
'''

from argparse import ArgumentParser, Namespace, _SubParsersAction

from books.books import Book
from books.commands.commands import Command
from books.database import BookDatabase


class Find(Command):
    parser: ArgumentParser

    def add_subparsers(self, subparsers: _SubParsersAction) -> None:
        find_parser = subparsers.add_parser(
            "find", help="Find books by title, author or year"
        )
        find_parser.add_argument(
            "-t", "--title", help="Title of the book to find"
        )
        find_parser.add_argument(
            "-a", "--author", help="Author of the book to find"
        )
        find_parser.add_argument(
            "-y", "--year", type=int, help="Year of publication to find"
        )
        self.parser = find_parser

    def __call__(self, db: BookDatabase, args: Namespace) -> None:
        if all([
            not args.title,
            not args.author,
            not args.year
        ]):
            self.parser.print_help()
        else:
            books = db.find_books(args.title, args.author, args.year)
            if not books:
                print("No books found.")
                return
            Book.print_list_books_as_table(books)
