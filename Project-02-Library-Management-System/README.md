# Project 02 - Library Management System

## About the Project

I created this Library Management System as my second mini-project in Python. The main purpose of this project is to manage books and members simply.

The system allows the user to add books and members, search for and update books, issue and return books, display available books, and save records to CSV files.

## What I Created

In this project, I created four classes:

* `Person` - Abstract class for common person information.
* `Member` - Inherits from `Person` and stores member details.
* `Book` - Stores book information and handles book issue and return.
* `Library_Management` - Handles the main library operations and menu.

## Features

* Add a new member
* Add a new book
* Search for a book
* Update book title
* Issue a book to a member
* Return a book
* Display available books
* Save book and member records
* Load saved records
* Handle invalid input

## OOP Concepts Used

### 1. Abstraction

I used the `ABC` and `abstractmethod` from the `abc` module.

The `Person` class is an abstract class, and the `display_info()` method is implemented in the `Member` class.

### 2. Inheritance

The `Member` class inherits common information from the `Person` class.

```python
class Member(Person):
```

### 3. Encapsulation

Private attributes are used for important data such as:

* Member ID
* Book ID
* Book title
* Author
* Book availability

Getters and setters are used to access and update the private data.

## File Handling

I used CSV files to store the records.

* `books.csv` stores book records.
* `members.csv` stores member records.

The program can save records to these files and load them again when required.

## Exception Handling

I used `try-except` blocks to handle errors such as:

* Entering invalid numeric values
* Missing CSV files

This prevents the program from stopping suddenly because of common input or file errors.

## What I Practiced

While creating this project, I practiced:

* Python classes and objects
* Inheritance
* Abstraction
* Encapsulation
* Getters and setters
* Lists
* Loops and conditions
* Functions and methods
* CSV file handling
* Exception handling
* Menu-driven programs

## Project Structure

```text
Project-02-Library-Management-System/
│
├── Library Management System.py
├── books.csv
├── members.csv
├── README.md
│
└── Screenshots/
    ├── 01-add-member.png
    ├── 02-add-book.png
    ├── 03-display-available-book.png
    ├── 04-search-book.png
    ├── 05-update-book.png
    ├── 06-issue-book.png
    ├── 07-return-book.png
    ├── 08-save-records.png
    ├── 09-load-records.png
    ├── 10-invalid-input.png
    └── 11-file-not-found.png
```

## How to Run

1. Open the project folder.
2. Open `Library Management System.py`.
3. Run the Python file.
4. Use the menu options to perform different library operations.

## Technologies Used

* Python
* CSV
* Object-Oriented Programming

## Screenshots

Screenshots of the different operations performed by the program are available in the `Screenshots` folder.

## Project Status

**Completed and tested.**
