import os
import shutil
from argparse import ArgumentParser
from unittest.mock import patch

from pytest import mark, raises
from tests.database.test_database import (
    db_fixture_created_path,
    db_fixture_full_path,
)

from books.commands.crud import Add, Clear, List, Remove, Update
from books.database import BookDatabase


class DynamicObject:
    pass


def create_any_parser(cls: type):
    main_parser = ArgumentParser()
    subparsers = main_parser.add_subparsers()
    parser = cls('name', 'description')
    parser.add_subparsers(subparsers)
    return parser


@mark.parametrize("cls", [Add, Clear, List, Remove, Update])
def test__commands__add_subparsers(cls):
    add_parser = create_any_parser(cls)

    assert hasattr(add_parser, "parser")
    assert isinstance(add_parser.parser, ArgumentParser)


def test__commands_add__call():
    db = BookDatabase(db_fixture_created_path, debug=True)

    add_parser = create_any_parser(Add)
    args = DynamicObject()
    args.title = 'детство'
    args.author = 'Толстой'
    args.year = 1868
    add_parser(db, args)


def test__commands_remove__call():
    shutil.copy(db_fixture_full_path, db_fixture_created_path)
    db = BookDatabase(db_fixture_created_path, debug=True)

    remove_parser = create_any_parser(Remove)
    args = DynamicObject()

    for i in range(1, 12):
        # 1-10 is valid id and 11 is invalid id
        args.id = i
        remove_parser(db, args)

    os.remove(db_fixture_created_path)


def test__commands_update__call():
    shutil.copy(db_fixture_full_path, db_fixture_created_path)
    db = BookDatabase(db_fixture_created_path, debug=True)

    update_parser = create_any_parser(Update)
    args = DynamicObject()

    for i in range(1, 12):
        args.id = i
        args.status = 'available'
        update_parser(db, args)

    for i in range(1, 12):
        args.id = i
        args.status = 'issued'
        update_parser(db, args)

    with raises(ValueError):
        for i in range(1, 12):
            args.id = i
            args.status = 'invalid'
            update_parser(db, args)

    os.remove(db_fixture_created_path)


def test__commands_list__call():
    shutil.copy(db_fixture_full_path, db_fixture_created_path)
    db = BookDatabase(db_fixture_created_path, debug=True)

    list_parser = create_any_parser(List)
    list_parser(db, DynamicObject())

    os.remove(db_fixture_created_path)


@mark.parametrize("return_input", ['y', 'n', 'any'])
def test__commands_clear__call(return_input):
    shutil.copy(db_fixture_full_path, db_fixture_created_path)
    db = BookDatabase(db_fixture_created_path, debug=True)

    clear_parser = create_any_parser(Clear)
    with patch('builtins.input', return_value=return_input):
        clear_parser(db, DynamicObject())

    os.remove(db_fixture_created_path)
