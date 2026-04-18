import pytest
from bank_account import BankAccount


def test_init():
    acc = BankAccount(100)
    assert acc._balance == 100


def test_deposit():
    acc = BankAccount()
    acc.deposit(50)
    assert acc._balance == 50


def test_invalid_deposit():
    acc = BankAccount()
    with pytest.raises(ValueError):
        acc.deposit(-10)


def test_withdraw():
    acc = BankAccount(100)
    acc.withdraw(40)
    assert acc._balance == 60


def test_overdraw():
    acc = BankAccount(50)
    with pytest.raises(ValueError):
        acc.withdraw(100)
