import pytest
from compressor import compress


def test_basic():
    assert compress("Meeting Notes") == "Mtng Nts"
    assert compress("HELLO World") == "HLL Wrld"


def test_empty_string():
    assert compress("") == ""


def test_no_vowels():
    assert compress("CS50") == "CS50"


def test_all_vowels():
    assert compress("aeiouAEIOU") == ""
