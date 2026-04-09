import csv

expenses = []


def add_expense():
    category = input("Enter category: ")
    amount = float(input("Enter amount: "))

    expense = {
        "category": category,
        "amount": amount
    }

    expenses.append(expense)
    print("Expense added successfully.\n")


def show_total():
    total = sum(item["amount"] for item in expenses)
    print(f"Total Expenses: {total}\n")


def show_expenses():
    if not expenses:
        print("No expenses recorded.\n")
        return

    for item in expenses:
        print(f"{item['category']} - {item['amount']}")
    print()


def save_to_csv():
    with open("expenses.csv", "w", newline="") as file:
        writer = csv.DictWriter(file, fieldnames=["category", "amount"])
        writer.writeheader()
        writer.writerows(expenses)

    print("Expenses saved to expenses.csv\n")


def main():
    while True:
        print("1. Add Expense")
        print("2. Show Total")
        print("3. View All Expenses")
        print("4. Save to CSV")
        print("5. Exit")

        choice = input("Choose an option: ")

        if choice == "1":
            add_expense()
        elif choice == "2":
            show_total()
        elif choice == "3":
            show_expenses()
        elif choice == "4":
            save_to_csv()
        elif choice == "5":
            break
        else:
            print("Invalid choice.\n")


if __name__ == "__main__":
    main()
