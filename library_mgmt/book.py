


class Book:
    def __init__(self, isbn, title, author, total_copies, available_copies):
        self.isbn = isbn
        self.title = title
        self.author = author
        self.total_copies = int(total_copies)
        self.available_copies = int(available_copies)

    def __display__():
        print("book class created")

    def __str__(self):
        return (
            f"Book(ISBN: {self.isbn}, Title: '{self.title}', Author: '{self.author}', "
            f"Total: {self.total_copies}, Available: {self.available_copies})"
        )
