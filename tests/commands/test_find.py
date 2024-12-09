import os
import shutil
from argparse import ArgumentParser

from tests.database.test_database import (
    db_fixture_created_path,
    db_fixture_full_path,
)

from books.commands.find import Find
from books.database import BookDatabase


class DynamicObject:
    pass


def create_find_parser():
    parser = ArgumentParser()
    subparsers = parser.add_subparsers()
    find = Find('find', 'Find a book by ID')
    find.add_subparsers(subparsers)
    return find


def test__find__add_subparsers():
    find_parser = create_find_parser()

    assert hasattr(find_parser, "parser")
    assert isinstance(find_parser.parser, ArgumentParser)


def test__find__call():
    shutil.copy(db_fixture_full_path, db_fixture_created_path)
    db = BookDatabase(db_fixture_created_path, debug=True)
    find_parser = create_find_parser()
    args = DynamicObject()

    args.title = None
    args.author = None
    args.year = None
    find_parser(db, args)

    args.title = 'детство'
    args.author = None
    args.year = None
    find_parser(db, args)

    args.title = None
    args.author = 'Толстой'
    args.year = None
    find_parser(db, args)

    args.title = None
    args.author = None
    args.year = 1852
    find_parser(db, args)

    args.title = 'детство'
    args.author = 'Толстой'
    args.year = 1852
    find_parser(db, args)

    args.title = 'детство'
    args.author = 'Пушкин'
    args.year = 1852
    find_parser(db, args)

    os.remove(db_fixture_created_path)
