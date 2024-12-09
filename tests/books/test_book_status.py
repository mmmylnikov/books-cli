from hypothesis import given
from hypothesis import strategies as st

from books.books import BookStatus


def test__book_status__str():
    assert str(BookStatus.AVAILABLE) == "available"
    assert str(BookStatus.ISSUED) == "issued"


def test__book_status__repr():
    assert repr(BookStatus.AVAILABLE) == "available"
    assert repr(BookStatus.ISSUED) == "issued"


@given(value=st.sampled_from(["available", "issued"]))
def test__book_status__str__with_hypothesis(value: str):
    assert str(BookStatus(value)) == value
