# 🔐 Password Validator

## 📌 Description
This Python program validates a user password. The password must meet specific criteria, such as length, inclusion of numbers, uppercase letters, and special characters. Invalid passwords trigger exception messages until the user provides a valid one.

---

## 🚀 Features
- Minimum 6 characters
- Must contain at least one number
- Must contain at least one uppercase letter
- Must contain at least one special character (`!@#`)
- Handles invalid passwords using custom exceptions
- Loops until valid password is entered

---

## 🧠 Concepts Used
- Exception handling (`try` / `except`)
- Loops (`while True`)
- Input validation
- Custom error messages (`raise ValueError`)
- String methods (`isdigit()`, `isupper()`)

---

## ⚙️ How It Works
1. User enters a password.
2. The program checks:
   - Length ≥ 6
   - Contains at least one number
   - Contains at least one uppercase letter
   - Contains at least one special character (`!@#`)
3. If any condition fails, a `ValueError` is raised and caught, showing the user an error message.
4. If all conditions are met, the password is accepted, and the program exits.

---

## ▶️ Example
Enter password: abc
Error: Password must be at least 6 characters.

Enter password: abcdef
Error: Password must contain at least one number.

Enter password: abc123
Error: Password must contain at least one uppercase letter.

Enter password: Abc123
Error: Password must contain at least one special character (!@#).

Enter password: Abc123!
Password accepted!


---

## 🛠️ Technologies
- Python 3

---

## ✍️ Author
Caroline Mildred Gomes
