import os
import shutil

from hypothesis import given
from pytest import raises
from tests.books.test_book import books_strategy

from books.books import Book, BookStatus
from books.database import BookDatabase


db_fixture_full_path = 'tests/database/fixture/db_full.json'
db_fixture_empty_path = 'tests/database/fixture/db_empty.json'
db_fixture_created_path = 'tests/database/fixture/db_created.json'


def test__database__init_full():
    db = BookDatabase(db_fixture_full_path)
    assert isinstance(db, BookDatabase)
    assert db.next_id == 11
    assert len(db.get_books()) == 10


def test__database__init_empty():
    db = BookDatabase(db_fixture_empty_path)
    assert isinstance(db, BookDatabase)
    assert db.next_id == 1
    assert len(db.get_books()) == 0


def test__database__init_created():
    assert not os.path.exists(db_fixture_created_path)

    db = BookDatabase(db_fixture_created_path)
    assert isinstance(db, BookDatabase)
    assert db.next_id == 1
    assert len(db.get_books()) == 0


def test__database__save():
    db = BookDatabase(db_fixture_created_path)
    db.save()

    assert os.path.exists(db_fixture_created_path)

    os.remove(db_fixture_created_path)


@given(books_data=books_strategy)
def test__database__add_book(books_data):
    db = BookDatabase(db_fixture_created_path, debug=True)

    for book_id, book_data in enumerate(books_data, start=1):
        book = Book(
            id=None, title=book_data[1], author=book_data[2], year=book_data[3]
        )
        db.add_book(book)
        assert db.next_id == book_id + 1
        assert len(db.books.keys()) == book_id


def test__database__clear_books():
    shutil.copyfile(db_fixture_full_path, db_fixture_created_path)
    db = BookDatabase(db_fixture_created_path, debug=True)
    assert len(db.books.keys()) == 10

    db.clear_books()
    assert len(db.books.keys()) == 0

    os.remove(db_fixture_created_path)


def test__database__remove_book():
    shutil.copyfile(db_fixture_full_path, db_fixture_created_path)
    db = BookDatabase(db_fixture_created_path, debug=True)
    assert len(db.books.keys()) == 10

    # remove existing book
    for i in range(1, 11):
        book = db.remove_book(i)
        assert book is not None

    assert len(db.books.keys()) == 0

    # remove non-existing book
    for i in range(1, 11):
        book = db.remove_book(i)
        assert book is None

    os.remove(db_fixture_created_path)


def test__database__update_book():
    shutil.copyfile(db_fixture_full_path, db_fixture_created_path)
    db = BookDatabase(db_fixture_created_path, debug=True)
    assert len(db.books.keys()) == 10

    for i in range(1, 11):
        book = db.update_book_status(i, BookStatus.AVAILABLE)
        assert book.status == BookStatus.AVAILABLE

    for i in range(1, 11):
        book = db.update_book_status(i, BookStatus.ISSUED)
        assert book.status == BookStatus.ISSUED

    for i in range(21, 31):
        book = db.update_book_status(i, object())
        assert book is None

    for i in range(1, 11):
        with raises(ValueError):
            book = db.update_book_status(i, 'not_valid')

    os.remove(db_fixture_created_path)


def test__database__find_books():
    shutil.copyfile(db_fixture_full_path, db_fixture_created_path)
    db = BookDatabase(db_fixture_created_path, debug=True)
    assert len(db.books.keys()) == 10

    books = db.find_books(title='детство')
    assert len(books) == 1

    books = db.find_books(author='Толстой')
    assert len(books) == 3

    books = db.find_books(year=1868)
    assert len(books) == 2

    books = db.find_books(author='Толстой', year=1868)
    assert len(books) == 1

    os.remove(db_fixture_created_path)
