username = "admin"
password = "1234"

attempts = 0

while attempts < 3:
    try:
        u = input("Username: ")
        p = input("Password: ")

        if u != username or p != password:
            raise ValueError("Invalid credentials.")

        print("Login successful!")
        break

    except ValueError as e:
        print("Error:", e)
        attempts += 1

if attempts == 3:
    print("Account locked.")
