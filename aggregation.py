# Aggregation = relação has-a em que uma classe contém/referencia objetos de outra classe, mas esses objetos podem existir independentemente.

# the container
class Library:
    def __init__(self, name):
        self.name = name
        self.books = []

    def add_book(self, book):
        self.books.append(book)

    def list_books(self):
        return [book.title for book in self.books]

# independent pat
class Book:
    def __init__(self, title, author):
        self.title = title
        self.author = author

library = Library("New York Public Library")

book1 = Book("Harry Potter", "J.K Rowling")
book2 = Book("The Hobbit", "J.R.R Tolkein")
book3 = Book("Call me by your name", "André Aciman")

# here the library HAS/CONTAINS the books for now,
# then the books can live without the library - INDEPENDENT
library.add_book(book1)
library.add_book(book2)
library.add_book(book3)


print(library.list_books())
# or
for book in library.list_books():
    print(book)
