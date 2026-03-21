balance = 1000

while True:
    try:
        amount = float(input("Enter amount to withdraw: "))

        if amount <= 0:
            raise ValueError("Amount must be positive.")

        if amount > balance:
            raise ValueError("Insufficient balance.")

        balance -= amount
        print(f"Withdrawal successful! Remaining balance: {balance}")
        break

    except ValueError as e:
        print("Error:", e)
