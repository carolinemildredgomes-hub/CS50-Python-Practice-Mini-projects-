import re


def strong(password):
    return bool(
        len(password) >= 8
        and re.search(r"[A-Z]", password)
        and re.search(r"[a-z]", password)
        and re.search(r"\d", password)
    )


def main():
    print(strong(input("Password: ")))


if __name__ == "__main__":
    main()
