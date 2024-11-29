# Book CLI Application Demo

This is a demo and documentation for the book CLI application.

## Table of Contents

- [Installation](#installation)
- [Run](#run)
  - [Show version](#show-version)
  - [Show help](#show-help)
- [Commands](#commands)
  - [add TITLE AUTHOR YEAR](#add-title-author-year)
  - [update BOOK_ID STATUS](#update-book_id-status)
  - [remove BOOK_ID](#remove-book_id)
  - [clear](#clear)
  - [list](#list)
  - [find -t TITLE -a AUTHOR -y YEAR](#find-t-title-a-author-y-year)

## Installation

First, you need to install the application:

```sh
$ git clone https://github.com/mmmylnikov/books-cli.git
```

## Run

For running the application, you need to run the following command:

```sh
$ cd books-cli
$ python -m books
```

### Show version

You can show the version of the application:

```sh
$ python -m books --version
books 1.0.0
```

### Show help

For showing help, you need to run the following command:

```sh
$ python -m books --help
```

Books application shows help content for each command.

```sh
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

## Commands

Each command is described in the following section.

### add TITLE AUTHOR YEAR

Add a new book. For adding a new book, you need to run the following command:

```sh
$ python -m books add "Война и мир" "Лев Толстой" 1868
```

First argument is the `title` of the book, second argument is the `author` of the book and third argument is the `year` of publication.

Application adds a new book to the database and displays a success message.

```sh
Book(id=1, title='Война и мир', author='Лев Толстой', year=1868, status=available) added successfully.
```

### update BOOK_ID STATUS

Update the status of a book. For updating the status of a book, you need to run the following command:

```sh bash
$ python -m books update 1 issued
```

First argument is the `id` of the book and second argument is the `status` of the book. Status can be `issued` or `available`.

Application updates the status of a book in the database and displays a success message:

```sh
Book(id=1, title='Война и мир', author='Лев Толстой', year=1868, status=issued) status updated successfully.
```

If the book is not found or the status is not valid, the application displays an error message:

```sh
$ python -m books update 2 issued
Book with ID 2 not found.

$ python -m books update 1 missing
usage: books update [-h] id {available,issued}
books update: error: argument status: invalid choice: 'missing' (choose from 'available', 'issued')
```

### remove BOOK_ID

Remove a book by ID. For removing a book, you need to run the following command:

```sh
$ python -m books remove 1
```

Application removes a book from the database and displays a success message:

```sh
Book(id=1, title='Война и мир', author='Лев Толстой', year=1868, status=issued) removed successfully.
```

If the book is not found, the application displays an error message:

```sh   
$ python -m books remove 2
Book with ID 2 not found.
```

### clear

Clear all books. For clearing all books, you need to run the following command:

```sh
$ python -m books clear
```

Application asks for confirmation before removing all books from the database and displays a success message:

```sh
Are you sure? [y/N]: 
```

If the user confirms, the application clears all books from the database and displays a success message:

```sh
All books cleared.
```

### list

List all books. For listing all books, you need to run the following command:

```sh
$ python -m books list
```

Application displays a list of all books in the database:

```sh
  id title                     author                    year status    
-------------------------------------------------------------------------------
   1 Война и мир               Лев Толстой               1868 available 
   2 Анна Каренина             Лев Толстой               1875 available 
   3 Детство                   Лев Толстой               1852 available 
   4 Преступление и наказание  Федор Достоевский         1866 available 
   5 Идиот                     Федор Достоевский         1868 available 
   6 Братья Карамазовы         Федор Достоевский         1879 issued    
   7 Мертвые души              Николай Гоголь            1842 available 
   8 Тарас Бульба              Николай Гоголь            1835 issued    
   9 Капитанская дочка         Александр Пушкин          1836 available 
  10 Евгений Онегин            Александр Пушкин          1823 issued   
```

### find -t TITLE -a AUTHOR -y YEAR

Find books by title, author or year. For finding books, you can run the following commands (use one or more of arguments):

```sh
$ python -m books find -t "Война и мир"
  id title                     author                    year status    
-------------------------------------------------------------------------------
   1 Война и мир               Лев Толстой               1868 available 

$ python -m books find -a "Достоевский"
  id title                     author                    year status    
-------------------------------------------------------------------------------
   4 Преступление и наказание  Федор Достоевский         1866 available 
   5 Идиот                     Федор Достоевский         1868 available 
   6 Братья Карамазовы         Федор Достоевский         1879 issued    

$ python -m books find -y 1868
  id title                     author                    year status    
-------------------------------------------------------------------------------
   1 Война и мир               Лев Толстой               1868 available 
   5 Идиот                     Федор Достоевский         1868 available 

$ python -m books find  -a "Лев Толстой" -y 1868
  id title                     author                    year status    
-------------------------------------------------------------------------------
   1 Война и мир               Лев Толстой               1868 available 
```

If the book is not found, the application displays an error message:

```sh   
$ python -m books find -t "Евгений Онегин" -a "Николай Гоголь"
No books found.
```