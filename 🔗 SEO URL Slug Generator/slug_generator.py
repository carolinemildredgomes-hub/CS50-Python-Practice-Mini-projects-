import re


def slugify(title):
    title = title.lower().strip()
    title = re.sub(r"\s+", "-", title)
    title = re.sub(r"[^a-z0-9-]", "", title)
    return title


def main():
    print(slugify(input("Title: ")))


if __name__ == "__main__":
    main()
