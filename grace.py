class Book:
    def __init__(self, title, author):
        self.title = title
        self.author = author
        self.is_available = True

class Library:
    def __init__(self):
        self.books = []

    def add_book(self, book):
        self.books.append(book)

    def display_books(self):
        for index, book in enumerate(self.books, start=1):
            status = "Available" if book.is_available else "Not Available"
            print(f"{index}. {book.title} by {book.author} - {status}")

    def borrow_book(self, book_index):
        if 1 <= book_index <= len(self.books):
            book = self.books[book_index - 1]
            if book.is_available:
                book.is_available = False
                print(f"You've borrowed '{book.title}'. Enjoy reading!")
            else:
                print("Sorry, the book is not available.")
        else:
            print("Invalid book index.")

    def return_book(self, book_index):
        if 1 <= book_index <= len(self.books):
            book = self.books[book_index - 1]
            if not book.is_available:
                book.is_available = True
                print(f"Thank you for returning '{book.title}'.")
            else:
                print("This book is already available in the library.")
        else:
            print("Invalid book index.")

def main():
    library = Library()

    book1 = Book("The Catcher in the Rye", "J.D. Salinger")
    book2 = Book("To Kill a Mockingbird", "Harper Lee")
    book3 = Book("1984", "George Orwell")

    library.add_book(book1)
    library.add_book(book2)
    library.add_book(book3)

    while True:
        print("\nLibrary Management System")
        print("1. Display Books")
        print("2. Borrow Book")
        print("3. Return Book")
        print("4. Exit")

        choice = input("Enter your choice: ")

        if choice == "1":
            library.display_books()
        elif choice == "2":
            book_index = int(input("Enter the index of the book you want to borrow: "))
            library.borrow_book(book_index)
        elif choice == "3":
            book_index = int(input("Enter the index of the book you want to return: "))
            library.return_book(book_index)
        elif choice == "4":
            print("Exiting the system.")
            break
        else:
            print("Invalid choice. Please choose a valid option.")

if __name__ == "__main__":
    main()
