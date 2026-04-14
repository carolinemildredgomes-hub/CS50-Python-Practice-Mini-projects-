import re


def format_number(number):
    match = re.fullmatch(r"(\d{3})(\d{3})(\d{4})", number)

    if not match:
        return None

    return f"({match.group(1)}) {match.group(2)}-{match.group(3)}"


def main():
    print(format_number(input("Number: ")))


if __name__ == "__main__":
    main()
