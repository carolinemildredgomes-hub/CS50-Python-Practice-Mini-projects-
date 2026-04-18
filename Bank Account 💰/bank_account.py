class BankAccount:
    def __init__(self, balance=0):
        if balance < 0:
            raise ValueError("Invalid balance")
        self._balance = balance

    def deposit(self, amount):
        if amount < 0:
            raise ValueError("Invalid amount")
        self._balance += amount

    def withdraw(self, amount):
        if amount > self._balance:
            raise ValueError("Insufficient funds")
        self._balance -= amount

    def __str__(self):
        return f"Balance: ${self._balance}"


def main():
    account = BankAccount()

    account.deposit(100)
    account.withdraw(30)

    print(account)


if __name__ == "__main__":
    main()
