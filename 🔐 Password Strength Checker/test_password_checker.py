from password_checker import strong


def test_valid():
    assert strong("Python123") is True


def test_invalid():
    assert strong("python") is False
