def main():
    code = input("Enter product code: ")
    print(is_valid(code))


def is_valid(code):
    """Validate product codes based on rules."""
    if len(code) < 2 or len(code) > 6:
        return False

    if not code[:2].isalpha():
        return False

    # Check numbers at the end only
    for i, char in enumerate(code[2:], start=2):
        if not char.isdigit():
            return False

    # First number cannot be 0 if numbers exist
    for char in code[2:]:
        if char.isdigit():
            if char == "0":
                return False
            break

    # No spaces or punctuation
    if not code.isalnum():
        return False

    return True


if __name__ == "__main__":
    main()
