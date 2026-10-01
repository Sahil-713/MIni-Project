# Student Management System

## About the Project

I created this Student Management System as my first mini project using Python.

The main purpose of this project was to practice the Python concepts I have been learning, especially **Object-Oriented Programming (OOP)**, file handling, and exception handling.

The project is a console-based application where student records can be added, displayed, searched, updated, and deleted. I also added the option to calculate the average marks of the students.

I used a CSV file to save the student records so that the data can be loaded again when the program is run.

## What I Created

I created the project using three classes:

* `Person` — an abstract base class for common person information.
* `Student` — inherits from `Person` and stores student details.
* `Student_Management` — handles the student records and all the main operations.

The program has a menu through which the user can select different operations.

## Features I Added

* Add a new student
* Display student details
* Search for a student using Student ID
* Update student marks
* Delete a student
* Calculate average marks
* Save student records to a CSV file
* Load records from the CSV file
* Handle invalid numeric input
* Handle a missing CSV file

## OOP Concepts I Used

### Abstraction

I created the `Person` class as an abstract class using `ABC` and `@abstractmethod`.

### Inheritance

The `Student` class inherits the common information from the `Person` class.

### Encapsulation

I used private attributes for important student information such as Student ID, Standard, and Marks.

### Getters and Setters

I used getter methods to access private values and a setter for marks. The setter also checks that marks are between 0 and 100.

## File Handling

I used Python's `csv` module to store student records in:

`students.csv`

The program can both save records to the file and load them back into the program.

## Exception Handling

I added exception handling so that the program does not stop when some common errors occur.

For example:

* `ValueError` is used when invalid numeric input is entered.
* `FileNotFoundError` is used when the `students.csv` file cannot be found.

## What I Practiced in This Project

While making this project, I practiced:

* Creating classes and objects
* Constructors
* Inheritance
* Abstraction
* Encapsulation
* Getters and setters
* Lists and loops
* Functions and methods
* CSV file handling
* Exception handling
* Building a menu-driven Python program

## Project Structure

```text
Project-01-Student-Management-System/
│
├── Student Management System.py
├── students.csv
├── README.md
└── Screenshots/
    ├── 01-invalid-input.png
    ├── 02-file-not-found.png
    ├── 03-add-student.png
    ├── 04-display-student.png
    ├── 05-search-student.png
    ├── 06-update-student.png
    ├── 07-delete-student.png
    ├── 08-average-marks.png
    ├── 09-save-records.png
    └── 10-load-records.png
```

## How to Run

Make sure Python is installed on your computer.

Open the project folder in the terminal and run:

```bash
python "Student Management System.py"
```

After running the program, the Student Management System menu will appear.

## Screenshots

The `Screenshots` folder contains screenshots of the different operations and error handling tested during the development of the project.

## Project Status

**Project 01 — Completed and Tested**
