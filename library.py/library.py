class Book:
    read_pages = 0

    def __init__(self, name, pages):
        self.name = name
        self.pages = pages
        

    def read_percent(self):
        return (self.read_pages / self.pages) * 100

    def __str__(self):
        return f"Книга: {self.name}\nКількість сторінок: {self.pages}\nПрочитано у відсотках: {self.read_percent()}%"

class Library:
    books_list = []

    def follow_book(self, book):
        self.books_list.append(book)

    def delete_book(self, name):
        self.books_list = [book for book in self.books_list if book.name != name]

    def print_books_list(self):
        for book in self.books_list:
            print(book)

library = Library()
book1 = Book('It 1', 60)
book1.read_pages = 100
book2 = Book('It 2', 300)
book2.read_pages = 100
book3 = Book('It 3', 400)
book3.read_pages = 100
book4 = Book('It 4', 500)
book4.read_pages = 100
library.follow_book(book1)
library.follow_book(book2)
library.follow_book(book3)
library.follow_book(book4)
library.print_books_list()
library.delete_book(book3.name)
library.print_books_list()
