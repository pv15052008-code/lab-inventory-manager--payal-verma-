import json
from book import Book

class LibraryInventory:
    def __init__(self, filename="books.json"):
        self.filename = filename
        self.books = []
        self.load_books()
    
    def load_books(self):
        try:
            with open(self.filename, 'r') as f:
                data = json.load(f)
                for book_data in data:
                    book = Book(book_data['title'], book_data['author'], book_data['isbn'])
                    book.status = book_data['status']
                    self.books.append(book)
        except FileNotFoundError:
            self.books = []
    
    def save_books(self):
        data = [book.to_dict() for book in self.books]
        with open(self.filename, 'w') as f:
            json.dump(data, f, indent=4)
    
    def add_book(self, title, author, isbn):
        for book in self.books:
            if book.isbn == isbn:
                print("ISBN already exists!")
                return False
        new_book = Book(title, author, isbn)
        self.books.append(new_book)
        self.save_books()
        return True
    
    def search_title(self, title):
        return [b for b in self.books if title.lower() in b.title.lower()]
    
    def search_isbn(self, isbn):
        for b in self.books:
            if b.isbn == isbn:
                return b
        return None
    
    def show_books(self):
        for i, book in enumerate(self.books, 1):
            print(f"{i}. {book}")