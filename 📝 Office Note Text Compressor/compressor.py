def main():
    text = input("Enter your office note: ")
    print(compress(text))


def compress(text):
    """Remove all vowels (A, E, I, O, U) from text."""
    vowels = "aeiouAEIOU"
    result = ""
    for char in text:
        if char not in vowels:
            result += char
    return result


if __name__ == "__main__":
    main()
