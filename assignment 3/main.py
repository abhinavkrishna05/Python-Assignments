# main.py
import sys
import os
sys.path.append(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))


from library_manager.inventory import LibraryInventory
from library_manager.book import Book

def menu():
    lib = LibraryInventory()

    while True:
        print("\n===== Library Menu =====")
        print("1. Add Book")
        print("2. View All Books")
        print("3. Search Book")
        print("4. Issue Book")
        print("5. Return Book")
        print("6. Exit")

        choice = input("Enter choice: ")

        if choice == "1":
            title = input("Title: ")
            author = input("Author: ")
            isbn = input("ISBN: ")

            new_book = Book(title, author, isbn)
            lib.add_book(new_book)
            print("Book added.\n")

        elif choice == "2":
            all_books = lib.display_all()
            if not all_books:
                print("No books available.")
            else:
                for b in all_books:
                    print(b)

        elif choice == "3":
            key = input("Enter title or ISBN: ")

            result_isbn = lib.search_by_isbn(key)
            result_title = lib.search_by_title(key)

            if result_isbn:
                print(result_isbn)
            elif result_title:
                for b in result_title:
                    print(b)
            else:
                print("Book not found.")

        elif choice == "4":
            isbn = input("Enter ISBN to issue: ")
            b = lib.search_by_isbn(isbn)
            if b and b.issue():
                lib.save_data()
                print("Book issued.")
            else:
                print("Cannot issue book.")

        elif choice == "5":
            isbn = input("Enter ISBN to return: ")
            b = lib.search_by_isbn(isbn)
            if b and b.return_book():
                lib.save_data()
                print("Book returned.")
            else:
                print("Cannot return book.")

        elif choice == "6":
            print("Goodbye!")
            break

        else:
            print("Invalid choice.")
def menu():
    ...
    # your menu code
    ...

if __name__ == "__main__":
    menu()

