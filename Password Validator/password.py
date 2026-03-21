while True:
    try:
        password = input("Enter password: ")

        if len(password) < 6:
            raise ValueError("Password must be at least 6 characters.")

        if not any(char.isdigit() for char in password):
            raise ValueError("Password must contain at least one number.")

        if not any(char.isupper() for char in password):
            raise ValueError("Password must contain at least one uppercase letter.")

        if not any(char in "!@#" for char in password):
            raise ValueError("Password must contain at least one special character (!@#).")

        print("Password accepted!")
        break

    except ValueError as e:
        print("Error:", e)
