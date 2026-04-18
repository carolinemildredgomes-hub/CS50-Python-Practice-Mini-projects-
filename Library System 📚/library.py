class Book:
    def __init__(self, title):
        self.title = title
        self.available = True

    def borrow(self):
        if not self.available:
            raise ValueError("Book not available")
        self.available = False

    def return_book(self):
        self.available = True

    def __str__(self):
        status = "Available" if self.available else "Borrowed"
        return f"{self.title} - {status}"


def main():
    book = Book("Python Basics")

    print(book)

    book.borrow()
    print(book)

    book.return_book()
    print(book)


if __name__ == "__main__":
    main()
