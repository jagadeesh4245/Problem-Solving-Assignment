# 🐍 Python OOP Practice Programs

A collection of beginner-friendly **Python Object-Oriented Programming (OOP)** practice programs designed to build a strong understanding of classes, objects, constructors, methods, attributes, conditional statements, and basic business logic.

This repository contains multiple practical examples that demonstrate how OOP concepts can be applied to real-world scenarios such as banking, employee management, shopping, billing, food ordering, movie tickets, patient records, and student performance.

## 📌 Topics Covered

* Classes and Objects
* `__init__()` Constructor
* Instance Variables
* Instance Methods
* Object Creation
* Conditional Statements
* Arithmetic Operations
* Percentage and Average Calculations
* Discount Calculations
* Salary and Bonus Calculations
* Banking Transactions
* Eligibility Checking
* Basic Data Processing

## 📂 Programs Included

| Program               | Description                                          |
| --------------------- | ---------------------------------------------------- |
| 🎓 Student            | Stores and displays student details                  |
| 👨‍💼 Employee        | Displays employee salary information                 |
| 🏦 Bank Account       | Deposit, withdraw, and check balance                 |
| 📱 Mobile             | Stores and displays mobile details                   |
| 📐 Rectangle          | Calculates area and perimeter                        |
| 📊 Student Result     | Checks pass/fail based on marks                      |
| 💰 Employee Bonus     | Calculates bonus based on salary                     |
| 🛒 Product Discount   | Calculates discounts based on product price          |
| 🏧 ATM                | Performs deposit, withdrawal, and balance operations |
| 🚗 Car                | Displays car information and categorizes price       |
| ⚡ Electricity Bill    | Calculates electricity bill based on units           |
| 📚 Book               | Demonstrates borrowing and returning books           |
| 🛍️ Shopping Cart     | Calculates product totals and shopping amount        |
| 📈 Employee Increment | Calculates salary increment based on rating          |
| 💳 Bank Account       | Demonstrates minimum balance validation              |
| 🍽️ Food Order        | Calculates order total and applicable discount       |
| 🏥 Patient            | Maintains patient information and medical bills      |
| 🧑‍💼 Attendance      | Calculates attendance percentage and eligibility     |
| 🎬 Movie Ticket       | Calculates ticket cost and bulk-ticket discount      |
| 📋 Student Report     | Calculates total, average, and grade                 |

## 🛠️ Technologies Used

* **Python 3**
* Object-Oriented Programming
* Conditional Statements
* Basic Mathematical Operations

## 🚀 How to Run

### 1. Clone the repository

```bash
git clone https://github.com/your-username/python-oop-practice.git
```

### 2. Navigate to the project

```bash
cd python-oop-practice
```

### 3. Run the Python file

```bash
python 22-9-26.py
```

## 💡 Example

One of the programs demonstrates a simple `BankAccount` class with deposit and withdrawal operations:

```python
class BankAccount:
    def __init__(self, account_holder, balance):
        self.account_holder = account_holder
        self.balance = balance

    def deposit(self, amount):
        self.balance = self.balance + amount

    def withdraw(self, amount):
        if amount > self.balance:
            print("Insufficient Balance")
        else:
            self.balance = self.balance - amount
```

This demonstrates how **attributes and methods** can be combined inside a class to model a real-world entity.

## 🎯 Purpose

The main purpose of this repository is to practice Python OOP concepts through simple, practical examples. These programs are useful for beginners who are learning Python and preparing for coding interviews, academic assignments, or entry-level programming exercises.

## 📈 Learning Outcomes

After completing these programs, you can understand and implement:

* How to create classes and objects
* How constructors initialize object data
* How instance methods work
* How to store and manipulate object attributes
* How to apply conditions inside class methods
* How to perform calculations using object data
* How to model simple real-world problems using OOP

## 👨‍💻 Author

**Jagadeesh**

Learning Python, Data Analytics, AI & Software Development.

---

⭐ If you find this repository useful, consider giving it a star!
