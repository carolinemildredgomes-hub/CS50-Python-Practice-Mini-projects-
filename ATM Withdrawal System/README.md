# 🏦 ATM Withdrawal System

## 📌 Description
This Python program simulates an ATM withdrawal system. It allows the user to withdraw money from a fixed balance while ensuring all input is valid.

---

## 🚀 Features
- Fixed balance ($1000)
- Input validation for numbers
- Prevent negative or zero withdrawals
- Prevent overdrafts
- Custom error messages for invalid inputs

---

## 🧠 Concepts Used
- Exception handling (`try` / `except`)
- Loops (`while True`)
- Conditional statements
- Custom error handling (`raise ValueError`)

---

## ⚙️ How It Works
1. User enters an amount to withdraw.
2. Program checks:
   - If amount is positive
   - If balance is sufficient
3. Errors handled using `ValueError`.
4. On valid input, balance is updated and displayed.

---

## ▶️ Example
Enter amount to withdraw: -50
Error: Amount must be positive.

Enter amount to withdraw: 1200
Error: Insufficient balance.

Enter amount to withdraw: 500
Withdrawal successful! Remaining balance: 500


---

## 🛠️ Technologies
- Python 3

---

## ✍️ Author
Caroline Mildred Gomes

