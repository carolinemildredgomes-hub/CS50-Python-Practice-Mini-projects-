from username_validator import validate

def test_valid():
    assert validate("Caroline_1") is True

def test_invalid():
    assert validate("1Caroline") is False
    assert validate ("ab") is False
