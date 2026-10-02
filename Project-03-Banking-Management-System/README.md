# 🏦 Project 3 — Banking Management System

## 📌 Project Overview

The **Banking Management System** is a Python-based console application developed to simulate basic banking operations.

The system allows customers to manage their bank accounts using a **unique account number and PIN**. Authentication is required before accessing protected banking operations.

The project provides functionality for checking account balances, depositing money, withdrawing money, and handling common errors such as an incorrect PIN or an account that does not exist.

This project was developed to practice **Python programming, Object-Oriented Programming (OOP), file handling, data management, authentication, and error handling**.

---

## ✨ Features

* 👤 Customer and account management
* 🔢 Unique account number for each account
* 🔐 PIN-based authentication
* 💰 Check account balance
* ➕ Deposit money
* ➖ Withdraw money
* 🧾 Store transaction records
* 💾 Store account and customer information using CSV files
* ⚠️ Incorrect PIN validation
* ⚠️ Account-not-found validation
* 🛡️ Basic transaction security
* 📋 Menu-based console interface

---

## 🔐 Account Authentication

The system uses an **Account Number** and **PIN** to authenticate the customer before allowing access to protected banking operations.

For example:

```text
Enter Account Number: 10001
Enter PIN: 2222
```

If the entered PIN is incorrect, the system displays:

```text
Incorrect PIN.
```

If the entered account number does not exist, the system displays:

```text
Account not found.
```

This provides a basic layer of security for accessing customer account information and performing transactions.

---

## 💰 Banking Operations

### 1. Check Balance

Customers can check their current account balance after successfully passing the required authentication.

### 2. Deposit Money

Customers can deposit money into their account.

The deposited amount is added to the existing account balance, and the transaction can be recorded in the transaction data.

### 3. Withdraw Money

Customers can withdraw money from their account after authentication.

The system checks the available balance before processing the withdrawal.

### 4. Account Validation

Before performing an operation, the system checks whether the entered account number exists.

If the account does not exist, the system displays:

```text
Account not found.
```

### 5. PIN Validation

The system verifies the customer's PIN before allowing access to protected banking operations.

If the PIN is incorrect:

```text
Incorrect PIN.
```

---

## 🗂️ Data Storage

The project uses **CSV files** to store and manage information.

### `accounts.csv`

Stores account-related information such as account details and balance.

### `customers.csv`

Stores customer-related information.

### `transactions.csv`

Stores transaction-related information such as deposits and withdrawals.

Using separate CSV files helps organize customer, account, and transaction data independently.

---

## 🧪 Testing

The application was tested using different inputs to verify that the authentication and account validation features work correctly.

### Test 1 — Incorrect PIN

**Input:**

```text
Enter your choice: 3
Enter Account Number: 10001
Enter PIN: 2222
```

**Output:**

```text
Incorrect PIN.
```

**Purpose:**

This test verifies that the system rejects an incorrect PIN and prevents unauthorized access to the selected banking operation.

---

### Test 2 — Account Not Found

**Input:**

```text
Enter your choice: 4
Enter Account Number: 2222
Enter PIN: 2222
```

**Output:**

```text
Account not found.
```

**Purpose:**

This test verifies that the system correctly identifies an account number that does not exist in the banking records.

---

## 📚 Concepts Used

The project applies the following Python concepts:

* Python Programming
* Object-Oriented Programming (OOP)
* Classes and Objects
* Encapsulation
* Methods and Functions
* Conditional Statements
* Loops
* Exception Handling
* Input Validation
* File Handling
* CSV Data Management
* Authentication Logic

---

## 🧠 OOP Implementation

Object-Oriented Programming is used to organize the different components of the banking system.

### Encapsulation

Account and customer-related information is managed within the appropriate classes and methods.

This helps keep important information such as account details, PINs, and balances organized and controlled.

### Classes and Objects

Classes are used to represent different entities within the banking system, while objects are used to work with individual customers, accounts, and transactions.

### Methods

Different methods are used to perform banking operations such as:

```text
Account Authentication
Check Balance
Deposit Money
Withdraw Money
Transaction Management
```

This makes the program structured and easier to maintain.

---

## 🔄 Basic Working Flow

```text
Start
  ↓
Display Banking Menu
  ↓
Select Operation
  ↓
Enter Account Number
  ↓
Check Account
  ↓
Account Found?
  ├── No → Account Not Found
  │
  └── Yes
        ↓
     Enter PIN
        ↓
     Verify PIN
        ↓
   PIN Correct?
     ├── No → Incorrect PIN
     │
     └── Yes
           ↓
     Perform Operation
           ↓
     Update Account /
     Transaction Records
           ↓
     Return to Menu
           ↓
          Exit
```

---

## 📂 Project Structure

```text
Project-03-Banking-Management-System/
│
├── Screenshots/
│   ├── [Project screenshots]
│
├── Banking Managment System.py
├── accounts.csv
├── customers.csv
├── transactions.csv
└── README.md
```

---

## ▶️ How to Run

### 1. Clone the Repository

```bash
git clone <repository-url>
```

### 2. Open the Project Folder

```bash
cd Project-03-Banking-Management-System
```

### 3. Run the Python Program

```bash
python "Banking Management System.py"
```

Follow the instructions displayed in the terminal to interact with the banking system.

---

## 🎯 Project Objective

The main objective of this project is to develop a simple **Banking Management System** using Python while applying Object-Oriented Programming concepts.

The project demonstrates how a real-world-style application can handle:

* Customer information
* Bank accounts
* Account authentication
* PIN verification
* Balance management
* Deposits
* Withdrawals
* Transaction records
* CSV-based data storage
* Error handling and validation
