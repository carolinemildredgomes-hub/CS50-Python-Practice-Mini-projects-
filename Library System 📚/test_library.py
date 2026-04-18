import pytest
from library import Book


def test_book_creation():
    b = Book("Python")
    assert b.title == "Python"
    assert b.available is True


def test_borrow():
    b = Book("Python")
    b.borrow()
    assert b.available is False


def test_double_borrow():
    b = Book("Python")
    b.borrow()
    with pytest.raises(ValueError):
        b.borrow()


def test_return():
    b = Book("Python")
    b.borrow()
    b.return_book()
    assert b.available is True


def test_str():
    b = Book("Python")
    assert str(b) == "Python - Available"
