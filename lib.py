class Book:
    def __init__(self, title, author, isbn):
        self.title = title
        self.author = author
        self.isbn = isbn
        self.checked_out = False

class Library:
    def __init__(self):
        self.books = []

    def add_book(self, book):
        self.books.append(book)

    def remove_book(self, isbn):
        for book in self.books:
            if book.isbn == isbn:
                self.books.remove(book)
                return True
        return False

    def list_books(self):
        for book in self.books:
            status = "Available" if not book.checked_out else "Checked Out"
            print(f"Title: {book.title}, Author: {book.author}, ISBN: {book.isbn}, Status: {status}")

    def checkout_book(self, isbn):
        for book in self.books:
            if book.isbn == isbn:
                if not book.checked_out:
                    book.checked_out = True
                    return True
                else:
                    return False
        return False

    def return_book(self, isbn):
        for book in self.books:
            if book.isbn == isbn:
                if book.checked_out:
                    book.checked_out = False
                    return True
                else:
                    return False
        return False

def main():
    library = Library()

    while True:
        print("\nLibrary Management System")
        print("1. Add Book")
        print("2. Remove Book")
        print("3. List Books")
        print("4. Checkout Book")
        print("5. Return Book")
        print("6. Quit")

        choice = input("Enter your choice: ")

        if choice == "1":
            title = input("Enter book title: ")
            author = input("Enter author name: ")
            isbn = input("Enter ISBN: ")
            book = Book(title, author, isbn)
            library.add_book(book)
            print("Book added successfully!")

        elif choice == "2":
            isbn = input("Enter ISBN of the book to remove: ")
            if library.remove_book(isbn):
                print("Book removed successfully!")
            else:
                print("Book not found.")

        elif choice == "3":
            library.list_books()

        elif choice == "4":
            isbn = input("Enter ISBN of the book to checkout: ")
            if library.checkout_book(isbn):
                print("Book checked out successfully!")
            else:
                print("Book not available or already checked out.")

        elif choice == "5":
            isbn = input("Enter ISBN of the book to return: ")
            if library.return_book(isbn):
                print("Book returned successfully!")
            else:
                print("Book not checked out or not found.")

        elif choice == "6":
            print("Goodbye!")
            break

        else:
            print("Invalid choice. Please try again.")

if __name__ == "__main__":
    main()
