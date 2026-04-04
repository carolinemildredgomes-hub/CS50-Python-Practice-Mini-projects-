import pytest
from product_code import is_valid


def test_valid_codes():
    assert is_valid("AB12") is True
    assert is_valid("XY6") is True
    assert is_valid("CD99") is True


def test_invalid_length():
    assert is_valid("A") is False
    assert is_valid("ABCDEFG") is False


def test_invalid_start():
    assert is_valid("1AB2") is False
    assert is_valid("1XY") is False


def test_invalid_numbers():
    assert is_valid("AB01") is False
    assert is_valid("XY0") is False


def test_invalid_characters():
    assert is_valid("AB#1") is False
    assert is_valid("XY 9") is False
