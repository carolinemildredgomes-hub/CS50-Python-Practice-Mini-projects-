expenses = {}

while True:
    try:
        name = input("Expense name: ")

        if name == "done":
            break

        amount = float(input("Amount: "))

        if amount <= 0:
            raise ValueError("Amount must be positive.")

        expenses[name] = expenses.get(name, 0) + amount

    except ValueError as e:
        print("Error:", e)

total = sum(expenses.values())

print("\nExpenses:")
for item in expenses:
    print(f"{item}: {expenses[item]}")

print("Total:", total)
