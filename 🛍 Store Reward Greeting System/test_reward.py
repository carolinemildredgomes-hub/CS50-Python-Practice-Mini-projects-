import pytest
from reward import reward


def test_welcome():
    assert reward("Welcome customer") == 0
    assert reward("WELCOME!") == 0


def test_w_only():
    assert reward("what's up?") == 20
    assert reward("Whoa!") == 20


def test_others():
    assert reward("Hello") == 100
    assert reward("Good morning") == 100
