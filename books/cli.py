'''
This module provides the Books CLI
'''

import argparse

from books import __app_name__, __description__, __epilog__, __version__
from books.commands.commands import CommandGroup
from books.commands.crud import Add, Clear, List, Remove, Update
from books.commands.find import Find
from books.database import BookDatabase


def main() -> None:
    '''
    Entry point for the Books CLI
    '''

    db = BookDatabase()

    parser = argparse.ArgumentParser(
        prog=__app_name__,
        description=__description__,
        epilog=__epilog__)

    parser.add_argument(
        "-v", "--version", action="version", version="%(prog)s " + __version__
    )

    subparsers = parser.add_subparsers(
        dest="command", help="Available commands"
    )

    commands = CommandGroup(parser, db, [
        Add("add", "Add a new book"),
        Update("update", "Update the status of a book"),
        Remove("remove", "Remove a book by ID"),
        Clear("clear", "Clear all books"),
        List("list", "List all books"),
        Find("find", "Find a book by ID"),
    ])

    commands.add_subparsers(subparsers)

    args = parser.parse_args()

    commands.run_control_flow(args)
