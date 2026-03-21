# 📂 File Reader

## 📌 Description
This program allows a user to read the contents of a file. It handles missing files and empty files gracefully.

---

## 🚀 Features
- Input filename
- Handles FileNotFoundError
- Handles empty files
- Displays file content
- Loops until a valid file is provided

---

## 🧠 Concepts Used
- Exception handling
- Loops
- File I/O
- Conditional logic

---

## ⚙️ How It Works
1. User enters filename.
2. Program tries to open the file.
3. If file does not exist → FileNotFoundError
4. If file empty → raise ValueError
5. Valid file → display content and exit

---

## ▶️ Example

## ▶️ Example

Enter filename: abc.txt
File not found.

Enter filename: empty.txt
Error: File is empty.

Enter filename: notes.txt
Hello world!

---

## 🛠️ Technologies
- Python 3

---

## ✍️ Author
Caroline Mildred Gomes
