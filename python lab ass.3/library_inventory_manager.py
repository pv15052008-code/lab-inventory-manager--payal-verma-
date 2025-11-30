from inventory import LibraryInventory
from book import Book

class LibraryInventoryManager:
    def __init__(self):
        self.inventory = LibraryInventory()
    
    def add_new_book(self):
        title = input("Enter book title: ")
        author = input("Enter author: ")
        isbn = input("Enter ISBN: ")
        if self.inventory.add_book(title, author, isbn):
            print("Book added successfully!")
        else:
            print("Cannot add book!")
    
    def issue_book(self):
        isbn = input("Enter ISBN to issue: ")
        book = self.inventory.search_isbn(isbn)
        if book and book.issue_book():
            self.inventory.save_books()
            print("Book issued!")
        else:
            print("Cannot issue book!")
    
    def return_book(self):
        isbn = input("Enter ISBN to return: ")
        book = self.inventory.search_isbn(isbn)
        if book and book.return_book():
            self.inventory.save_books()
            print("Book returned!")
        else:
            print("Cannot return book!")
    
    def search_book(self):
        title = input("Enter title to search: ")
        results = self.inventory.search_title(title)
        if results:
            for book in results:
                print(book)
        else:
            print("No books found!")
    
    def display_all(self):
        print("All Books:")
        self.inventory.show_books()