from hypothesis import given
from hypothesis import strategies as st

from books.books import Book, BookStatus


id_strategy_integer = st.integers()
id_strategy_string = st.text(alphabet="0123456789")
title_strategy = st.text()
author_strategy = st.text()
year_strategy_integer = st.integers(min_value=0, max_value=3000)
year_strategy_string = st.text(alphabet="0123456789")
status_strategy_enum = st.sampled_from(
    [BookStatus.AVAILABLE, BookStatus.ISSUED]
)
status_strategy_string = st.sampled_from(["available", "issued"])
books_strategy = st.lists(
    st.tuples(
        id_strategy_integer,
        title_strategy,
        author_strategy,
        year_strategy_integer,
        status_strategy_enum,
    )
)


@given(books_data=books_strategy)
def test__book__to_dict(books_data):
    for book_data in books_data:
        book = Book(*book_data)
        assert book.to_dict() == {
            'id': book.id,
            'title': book.title,
            'author': book.author,
            'year': book.year,
            'status': book.status.value
        }


@given(books_data=books_strategy)
def test__book__from_dict(books_data):
    for book_data in books_data:
        book_dict = {
            'id': book_data[0],
            'title': book_data[1],
            'author': book_data[2],
            'year': book_data[3],
            'status': book_data[4],
        }
        book = Book.from_dict(book_dict)

        title_cleaned = book_data[1].strip().replace("\n", " ")
        author_cleaned = book_data[2].strip().replace("\n", " ")

        assert book.id == book_data[0]
        assert book.title == title_cleaned
        assert book.author == author_cleaned
        assert book.year == book_data[3]
        assert book.status == BookStatus(book_data[4])


@given(books_data=books_strategy)
def test__book__get_fields(books_data):
    for book_data in books_data:
        book = Book(*book_data)
        fields = book.get_fields()
        for field in fields:
            assert hasattr(book, field)


@given(books_strategy)
def test__book__print_list_books_as_table(books_data):
    books_list = [Book(*book_data) for book_data in books_data]
    table = Book.print_list_books_as_table(books_list)

    assert isinstance(table, str)

    table_row_count = table.count("\n")
    if not books_list:
        assert table_row_count == 2
    else:
        assert table_row_count == (2 + len(books_list))
