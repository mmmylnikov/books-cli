'''
Commands module provides the Command and CommandGroup classes
'''

from argparse import ArgumentParser, Namespace, _SubParsersAction
from typing import Any

from books.database import BookDatabase


class Command:
    parser: ArgumentParser
    name: str
    description: str

    def __init__(self, name: str, description: str) -> None:
        self.name = name
        self.description = description

    def __call__(self, db: BookDatabase, args: Namespace) -> Any:
        raise NotImplementedError

    def add_subparsers(self, subparsers: Any) -> None:
        raise NotImplementedError


class CommandGroup:
    parser: ArgumentParser
    db: BookDatabase
    commands: list[Command]

    def __init__(
        self, parser: ArgumentParser, db: BookDatabase, commands: list[Command]
    ) -> None:
        self.parser = parser
        self.db = db
        self.commands = commands

    def add_subparsers(self, subparsers: _SubParsersAction) -> None:
        for command in self.commands:
            command.add_subparsers(subparsers)

    def run_control_flow(self, namespace: Namespace) -> None:
        for command in self.commands:
            if namespace.command != command.name:
                continue
            command(self.db, namespace)
            break
        else:
            self.parser.print_help()
