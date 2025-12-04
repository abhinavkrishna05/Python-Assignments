import json
from pathlib import Path
import logging
from .book import Book

logging.basicConfig(
    filename="library.log",
    level=logging.INFO,
    format="%(asctime)s - %(levelname)s - %(message)s"
)

class LibraryInventory:
    def __init__(self, data_file="data/books.json"):
        self.data_file = Path(data_file)
        self.books = []
        self.load_from_file()

    def add_book(self, title, author, isbn):
        book = Book(title, author, isbn)
        self.books.append(book)
        logging.info(f"Book added: {title}")
        self.save_to_file()

    def search_by_title(self, title):
        return [b for b in self.books if b.title.lower() == title.lower()]

    def search_by_isbn(self, isbn):
        for b in self.books:
            if b.isbn == isbn:
                return b
        return None

    def display_all(self):
        return self.books

    def save_to_file(self):
        try:
            self.data_file.parent.mkdir(parents=True, exist_ok=True)
            with open(self.data_file, "w") as f:
                json.dump([b.to_dict() for b in self.books], f, indent=4)
        except Exception as e:
            logging.error(f"Error saving file: {e}")

    def load_from_file(self):
        try:
            if self.data_file.exists():
                with open(self.data_file, "r") as f:
                    data = json.load(f)
                    self.books = [Book(**item) for item in data]
            else:
                self.books = []
        except Exception as e:
            logging.error(f"Error loading file: {e}")
            self.books = []
