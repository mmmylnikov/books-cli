from argparse import ArgumentParser, Namespace, _SubParsersAction

from hypothesis import given
from hypothesis import strategies as st
from pytest import raises
from tests.database.test_database import db_fixture_empty_path

from books.commands.commands import Command, CommandGroup
from books.database import BookDatabase


class DinamiclyObject:
    pass


@given(name=st.text(), description=st.text())
def test__command__init(name, description):
    command = Command(name, description)

    assert command.name == name
    assert command.description == description


def test__command__call_not_implemented():
    command = Command("name", "description")

    with raises(NotImplementedError):
        command(None, None)


def test__command__add_subparsers_not_implemented():
    command = Command("name", "description")

    with raises(NotImplementedError):
        command.add_subparsers(None)


def test__command_group__init():
    parser = ArgumentParser()
    db = BookDatabase(db_fixture_empty_path, debug=True)
    commands = [Command("name", "description")]

    command_group = CommandGroup(parser, db, commands)

    assert command_group.parser == parser
    assert command_group.db == db
    assert command_group.commands == commands


def test__command_group__add_subparsers():
    parser = ArgumentParser()
    subparsers = parser.add_subparsers()
    db = BookDatabase(db_fixture_empty_path, debug=True)
    command = Command("name", "description")
    command.add_subparsers = lambda x: None
    commands = [command]

    command_group = CommandGroup(parser, db, commands)

    command_group.add_subparsers(subparsers)


class TestCommand(Command):
    def add_subparsers(self, subparsers: _SubParsersAction) -> None:
        add_parser = subparsers.add_parser(
            "test_command", help="help to test command"
        )
        add_parser.add_argument("test_arg", type=str, help="help to test arg")
        self.parser = add_parser

    def __call__(self, db: BookDatabase, args: Namespace) -> None:
        return None


def test__command_group__run_control_flow():
    parser = ArgumentParser()
    db = BookDatabase(db_fixture_empty_path, debug=True)
    command = TestCommand("test", "description")
    commands = [command]
    namespace = DinamiclyObject()
    command_group = CommandGroup(parser, db, commands)

    namespace.command = "another"
    command_group.run_control_flow(namespace)

    namespace.command = "test"
    command_group.run_control_flow(namespace)
