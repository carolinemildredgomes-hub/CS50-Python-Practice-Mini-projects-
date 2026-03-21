# 🧮 Simple Calculator

## 📌 Description
This Python program functions as a basic calculator. It accepts two numbers and an operator from the user, performs the calculation, and displays the result. Invalid inputs and division by zero are handled using exceptions.

---

## 🚀 Features
- Accepts integers and floating-point numbers
- Supports addition, subtraction, multiplication, and division
- Handles invalid numbers using `ValueError`
- Handles division by zero using `ZeroDivisionError`
- Loops until a valid calculation is performed

---

## 🧠 Concepts Used
- Exception handling (`try` / `except`)
- Loops (`while True`)
- Conditional statements for operator logic
- Input validation

---

## ⚙️ How It Works
1. The user enters the first number.
2. The user enters an operator (`+`, `-`, `*`, `/`).
3. The user enters the second number.
4. The program performs the calculation:
   - If the operator is invalid, it asks again.
   - If the input is invalid (non-numeric), it asks again.
   - If division by zero occurs, it asks again.
5. The valid result is displayed and the program ends.

---

## ▶️ Example

First number: abc
Invalid number. Please enter numeric values.

First number: 10
Operator (+, -, *, /): /
Second number: 0
Cannot divide by zero!

First number: 10
Operator (+, -, *, /): /
Second number: 2
Result: 5.0


---

## 🛠️ Technologies
- Python 3

---

## ✍️ Author
Caroline Mildred Gomes
