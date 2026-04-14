import re


def extract_email(text):
    match = re.search(r"[\w.-]+@[\w.-]+\.\w+", text)
    return match.group() if match else None


def main():
    print(extract_email(input("Resume text: ")))


if __name__ == "__main__":
    main()
