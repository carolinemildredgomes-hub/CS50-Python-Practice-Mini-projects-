import re


def validate(username):
    return bool(re.fullmatch(r"[A-Za-z][A-Za-z0-9_]{4,14}", username))


def main():
    print(validate(input("Username: ")))


if __name__ == "__main__":
    main()
