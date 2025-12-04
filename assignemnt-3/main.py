from library_manager.inventory import LibraryInventory

def menu():
    print("\n==== Library Inventory Manager ====")
    print("1. Add Book")
    print("2. Issue Book")
    print("3. Return Book")
    print("4. View All Books")
    print("5. Search Book")
    print("6. Exit")

def main():
    inventory = LibraryInventory()

    while True:
        menu()
        choice = input("Enter your choice: ")

        if choice == "1":
            title = input("Enter title: ")
            author = input("Enter author: ")
            isbn = input("Enter ISBN: ")
            inventory.add_book(title, author, isbn)
            print("Book added successfully.")

        elif choice == "2":
            isbn = input("Enter ISBN to issue: ")
            book = inventory.search_by_isbn(isbn)
            if book and book.issue():
                inventory.save_to_file()
                print("Book issued successfully.")
            else:
                print("Book not available!")

        elif choice == "3":
            isbn = input("Enter ISBN to return: ")
            book = inventory.search_by_isbn(isbn)
            if book and book.return_book():
                inventory.save_to_file()
                print("Book returned successfully.")
            else:
                print("Cannot return this book.")

        elif choice == "4":
            books = inventory.display_all()
            if books:
                for b in books:
                    print(b)
            else:
                print("No books found.")

        elif choice == "5":
            title = input("Enter title: ")
            results = inventory.search_by_title(title)
            if results:
                for b in results:
                    print(b)
            else:
                print("No matching book found.")

        elif choice == "6":
            print("Exiting... Goodbye!")
            break

        else:
            print("Invalid choice. Try again.")

if __name__ == "__main__":
    main()
