from abc import ABC, abstractmethod
import csv


# Abstract class for common person information
class Person(ABC):

    def __init__(self, name, age):
        self._name = name
        self._age = age

    # Child classes must implement this method
    @abstractmethod
    def display_info(self):
        pass


# Member class inherits from Person
class Member(Person):

    def __init__(self, member_id, name, age):
        super().__init__(name, age)

        # Private member ID
        self.__member_id = member_id

    # Display member information
    def display_info(self):
        print("Member ID:", self.__member_id)
        print("Name:", self._name)
        print("Age:", self._age)

    # Getter for member ID
    def get_member_id(self):
        return self.__member_id


# Book class stores information about books
class Book:

    def __init__(self, book_id, title, author):
        self.__book_id = book_id
        self.__title = title
        self.__author = author
        self.__available = True
        self.__issued_to = ""

    # Display book information
    def display_info(self):
        print("Book ID:", self.__book_id)
        print("Title:", self.__title)
        print("Author:", self.__author)

        if self.__available:
            print("Status: Available")
        else:
            print("Status: Issued")
            print("Issued To:", self.__issued_to)

    # Getter for book ID
    def get_book_id(self):
        return self.__book_id

    # Getter for title
    def get_title(self):
        return self.__title

    # Setter for title
    def set_title(self, title):
        self.__title = title

    # Getter for author
    def get_author(self):
        return self.__author

    # Getter for availability
    def get_available(self):
        return self.__available

    # Getter for issued member
    def get_issued_to(self):
        return self.__issued_to

    # Issue the book to a member
    def issue_book(self, member_id):
        if self.__available:
            self.__available = False
            self.__issued_to = member_id
            return True

        return False

    # Return the book
    def return_book(self):
        if not self.__available:
            self.__available = True
            self.__issued_to = ""
            return True

        return False


# Library Management handles books and members
class Library_Management:

    def __init__(self):
        self.books = []
        self.members = []

    # Add a new member
    def add_member(self):
        try:
            member_id = int(input("Enter Member ID: "))
            name = input("Enter Name: ")
            age = int(input("Enter Age: "))

            member = Member(member_id, name, age)
            self.members.append(member)

            print("Member added successfully.")

        except ValueError:
            print("Please enter valid numeric values.")

    # Add a new book
    def add_book(self):
        try:
            book_id = int(input("Enter Book ID: "))
            title = input("Enter Book Title: ")
            author = input("Enter Author Name: ")

            book = Book(book_id, title, author)
            self.books.append(book)

            print("Book added successfully.")

        except ValueError:
            print("Please enter a valid Book ID.")

    # Search for a book using Book ID
    def search_book(self):
        try:
            book_id = int(input("Enter Book ID to search: "))

            for book in self.books:
                if book.get_book_id() == book_id:
                    book.display_info()
                    return

            print("Book not found.")

        except ValueError:
            print("Please enter a valid Book ID.")

    # Update the title of an existing book
    def update_book(self):
        try:
            book_id = int(input("Enter Book ID to update: "))

            for book in self.books:
                if book.get_book_id() == book_id:
                    new_title = input("Enter new book title: ")
                    book.set_title(new_title)

                    print("Book updated successfully.")
                    return

            print("Book not found.")

        except ValueError:
            print("Please enter a valid Book ID.")

    # Issue a book to a member
    def issue_book(self):
        try:
            book_id = int(input("Enter Book ID to issue: "))
            member_id = int(input("Enter Member ID: "))

            member_found = False

            for member in self.members:
                if member.get_member_id() == member_id:
                    member_found = True
                    break

            if not member_found:
                print("Member not found.")
                return

            for book in self.books:
                if book.get_book_id() == book_id:

                    if book.issue_book(member_id):
                        print("Book issued successfully.")
                    else:
                        print("Book is already issued.")

                    return

            print("Book not found.")

        except ValueError:
            print("Please enter valid numeric values.")

    # Return a book
    def return_book(self):
        try:
            book_id = int(input("Enter Book ID to return: "))

            for book in self.books:
                if book.get_book_id() == book_id:

                    if book.return_book():
                        print("Book returned successfully.")
                    else:
                        print("Book is already available.")

                    return

            print("Book not found.")

        except ValueError:
            print("Please enter a valid Book ID.")

    # Display all available books
    def display_available_books(self):
        found = False

        for book in self.books:
            if book.get_available():
                book.display_info()
                print()
                found = True

        if not found:
            print("No books are currently available.")

    # Save book and member records
    def save_records(self):

        with open("books.csv", "w", newline="") as file:
            writer = csv.writer(file)

            writer.writerow([
                "Book_ID",
                "Title",
                "Author",
                "Available",
                "Issued_To"
            ])

            for book in self.books:
                writer.writerow([
                    book.get_book_id(),
                    book.get_title(),
                    book.get_author(),
                    book.get_available(),
                    book.get_issued_to()
                ])

        with open("members.csv", "w", newline="") as file:
            writer = csv.writer(file)

            writer.writerow([
                "Member_ID",
                "Name",
                "Age"
            ])

            for member in self.members:
                writer.writerow([
                    member.get_member_id(),
                    member._name,
                    member._age
                ])

        print("Records saved successfully.")

    # Load book and member records
    def load_records(self):
        try:

            with open("books.csv", "r", newline="") as file:
                reader = csv.DictReader(file)

                for row in reader:
                    book = Book(
                        int(row["Book_ID"]),
                        row["Title"],
                        row["Author"]
                    )

                    if row["Available"] == "False":
                        book.issue_book(int(row["Issued_To"]))

                    self.books.append(book)

            with open("members.csv", "r", newline="") as file:
                reader = csv.DictReader(file)

                for row in reader:
                    member = Member(
                        int(row["Member_ID"]),
                        row["Name"],
                        int(row["Age"])
                    )

                    self.members.append(member)

            print("Records loaded successfully.")

        except FileNotFoundError:
            print("Required CSV file not found.")

    # Display the main menu
    def menu(self):

        while True:
            print("\n--- Library Management System ---")
            print("1. Add Member")
            print("2. Add Book")
            print("3. Search Book")
            print("4. Update Book")
            print("5. Issue Book")
            print("6. Return Book")
            print("7. Display Available Books")
            print("8. Save Records")
            print("9. Load Records")
            print("10. Exit")

            choice = input("Enter your choice: ")

            if choice == "1":
                self.add_member()

            elif choice == "2":
                self.add_book()

            elif choice == "3":
                self.search_book()

            elif choice == "4":
                self.update_book()

            elif choice == "5":
                self.issue_book()

            elif choice == "6":
                self.return_book()

            elif choice == "7":
                self.display_available_books()

            elif choice == "8":
                self.save_records()

            elif choice == "9":
                self.load_records()

            elif choice == "10":
                print("Program ended.")
                break

            else:
                print("Invalid choice. Please try again.")


# Start the Library Management System
system = Library_Management()
system.menu()