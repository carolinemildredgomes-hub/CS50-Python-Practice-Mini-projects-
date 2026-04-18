import pytest
from student_manager import Student


def test_valid_student():
    s = Student("Alice", "Red")
    assert s.name == "Alice"
    assert s.house == "Red"


def test_invalid_name():
    with pytest.raises(ValueError):
        Student("", "Red")


def test_invalid_house():
    with pytest.raises(ValueError):
        Student("Alice", "Yellow")


def test_str():
    s = Student("Bob", "Blue")
    assert str(s) == "Bob from Blue"
