class Book:
    def __init__(self, title, author):
        self.title = title
        self.author = author

    def display_book_details(self):
        print("Title:", self.title)
        print("Author:", self.author)


class IssuedBook(Book):
    def __init__(self, title, author, issued_to, issued_date):
        super().__init__(title, author)

        self.issued_to = issued_to
        self.issued_date = issued_date

    def display_issued_book_details(self):
        self.display_book_details()

        print("Issued To:", self.issued_to)
        print("Issued Date:", self.issued_date)



book1 = IssuedBook(
    "Python Programming",
    "Guido van Rossum",
    "Ibbani",
    "02-02-2026"
)

book1.display_issued_book_details()