# 👤 Username Validator System

A recruiter-friendly Python validation project designed to simulate real-world signup and authentication systems.

This project validates usernames based on predefined professional rules.

---

## 📌 Features

- Username must begin with a letter
- Can contain letters, numbers, and underscore
- Length must be 5–15 characters
- Regex-based validation
- Unit tested with pytest

---

## 📌 Tech Used

- Python
- Regular Expressions
- Pytest

---

## 📌 How It Works

The program accepts a username input and checks whether it follows valid system rules.

Example:

```text
Caroline_1 → True
1Caroline → False
```

---

## 📌 Run

```bash
python username_validator.py
```

---

## 📌 Test

```bash
pytest test_username_validator.py
```

---

## 👩‍💻 Author

Caroline Mildred Gomes
