# Books CLI Application

**books** is a command-line interface application built with [argparse](https://docs.python.org/3/library/argparse.html) (python standard library) to help you manage your library of books.

## Requirements

- [Python 3.12](https://www.python.org/) 

Optional (for development):
- [Flake8](https://pypi.org/project/flake8/) - style checking
- [Mypy](https://pypi.org/project/mypy/) - type checking
- [Isort](https://pypi.org/project/isort/) - import sorting
- [Pytest](https://pypi.org/project/pytest/), [pytest-cov](https://pypi.org/project/pytest-cov/), [hypothesis](https://pypi.org/project/hypothesis/) - unit testing
- [VHS](https://github.com/charmbracelet/vhs) - demo gif animation (later, keep tuned)

## Installation

To run **books**, you need to run the following steps:

1. Download the application's source code 

```sh
$ git clone https://github.com/mmmylnikov/books-cli.git
```

2. Go to the application's directory

```sh
$ cd books-cli/
```

3. Run the following command

```sh
$ python -m books -v
books 1.0.0
```

This command prints the application's version number.



## Usage

Once you've download the source code and run the installation steps, you can run the following command to access the application's usage description:

```sh
$ python -m books --help
usage: books [-h] [-v] {add,update,remove,clear,list,find} ...

Books CLI Application

positional arguments:
  {add,update,remove,clear,list,find}
                        Available commands
    add                 Add a new book
    update              Update the status of a book
    remove              Remove a book by ID
    clear               Clear all books
    list                List all books
    find                Find books by title, author or year

options:
  -h, --help            show this help message and exit
  -v, --version         show program's version number and exit

Books is a command-line interface application built with argparse (https://docs.python.org/3/library/argparse.html) to help you manage your library of books.
```

You can also access the help message for specific commands by typing the command and then `--help` or `-h`. For example, to display the help content for the `add` command, you can run the following:

```sh
$ python -m books add -h
usage: books add [-h] title author year

positional arguments:
  title       Title of the book
  author      Author of the book
  year        Year of publication

options:
  -h, --help  show this help message and exit
```

Calling `--help` on each command provides specific and useful information about how to use the command at hand.

## Features

**Books** has the following features:

| Command                           | Description                                                  |
| ----------------------------------| ------------------------------------------------------------ |
| `add TITLE AUTHOR YEAR`           | Adds a new book to the database.                             |
| `update BOOK_ID STATUS`           | Updates the status of a book using its `BOOK_ID`.            |
| `remove BOOK_ID`                  | Removes a book from the database using its `BOOK_ID`.        |
| `clear`                           | Clears all books from the database.                          |
| `list`                            | Lists all books in the database.                             |
| `find -t TITLE -a AUTHOR -y YEAR` | Finds books by title, author or year.                        |

You can find more information about each command on [documentation page](docs/doc.md).


## Development

To develop **books**, you need to run the following steps:

1. Download the application's source code

```sh
$ git clone https://github.com/mmmylnikov/books-cli.git
```

2. Create a Python virtual environment and activate it

```sh
$ cd books-cli/
$ python -m venv .venv
$ source .venv/bin/activate
(.venv) $
```

3. Install the dependencies

```sh
(.venv) $ python -m pip install -r requirements_dev.txt
```

4. Make your changes

5. Check style and types

Flake8 and Mypy are used to check the code's style and types. At the same time, imports are sorted using isort.

```sh
$ make check
```

6. Run tests

```sh
$ make test
```

## Release History

- 1.0.0
  + cli implementation using argparse (standard library)
  + database implementation using json (standard library)
  + `add`, `update`, `remove`, `clear`, `list`, `find` commands
  + `--version` and `--help` options
  + documentation and usage guide
  + database template from books by Russian writers
  + flake8 check code style
  + mypy check types
  + unit tests by Pytest and Hypothesis with coverage 99.6%
  + CI workflow with GitHub Actions (style, types, tests)

## TODO

### Description

It is necessary to develop a console application for managing a library of books. The application should allow you to add, delete, search and display books. Each book must contain the following fields:

- id (unique identifier, generated automatically)
- title (book title)
- author (book author)
- year (year of publication)
- status (book status: “available", “issued")

### Requirements

- [+] Adding a book: The user enters title, author and year, after which the book is added to the library with a unique id and the status "available".
- [+] Deleting a book: The user enters the ID of the book to be deleted.
- [+] Book Search: The user can search for books by title, author or year.
- [+] Displaying all books: The application displays a list of all books with their id, title, author, year and status.
- [+] Changing the status of the book: The user enters the ID of the book and the new status (“available” or “issued").

### Additional requirements
- [+] Implement data storage in a json format.
- [+] Ensure correct error handling (for example, an attempt to delete a non-existent book).
- [+] Write functions for each operation (add, remove, find, list, update status).
- [+] Do not use third-party libraries (with the exception of libraries for type checking (mypi), style checking (flake8), import sorting (isort) necessary for comfortable development).

### Evaluation criteria:
- [+] Correctness and completeness of the functional implementation.
- [+] Purity and readability of the code.
- [+] Error and exception handling.
- [+] Ease of use of the command line interface.
- [+] The structure of the project.

### It will be a plus:
- [+] Annotations: Annotation of functions and variables in the code (mypy check).
- [+] Functional description: A detailed description of the application's functionality in the README file.
- [+] Object-oriented programming approach (where appropriate).
- [+] Documentation: 
  + Detailed documentation of the application in the [docs page](docs/doc.md)
  + A short description of the project in the [README.md](README.md)
  + Help messages for using (for example, `python -m books -h`)
  + Help messages for commands in the application (for example, `python -m books add -h`)

## About the Author

Max Mylnikov - Telegram: [@mmmylnikov](https://t.me/mmmylnikov)

## License

Books is distributed under the [MIT License](LICENSE).

