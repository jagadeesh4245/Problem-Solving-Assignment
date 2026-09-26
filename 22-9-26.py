class Student:
    def __init__(self,name,age,course):
        self.name=name
        self.age=age
        self.course=course
    def display(self):
        print("Name:", self.name)
        print("Age:", self.age)
        print("Course:", self.course)
student1=Student("jagadeesh",22,"Data Analytics with Ai")
student1.display()

class Employee:
    def __init__(self, name, basic_salary):
        self.name = name
        self.basic_salary = basic_salary

    def display_salary(self):
        print("Name:", self.name)
        print("Salary:", self.basic_salary)


employee1 = Employee("Aparna", 30000)
employee1.display_salary()

class BankAccount:
    def __init__(self, account_holder, balance):
        self.account_holder = account_holder
        self.balance = balance

    def deposit(self, amount):
        self.balance = self.balance + amount
        print("Deposited:", amount)

    def withdraw(self, amount):
        if amount > self.balance:
            print("Insufficient Balance")
        else:
            self.balance = self.balance - amount
            print("Withdrawn:", amount)

    def display_balance(self):
        print("Account Holder:", self.account_holder)
        print("Balance:", self.balance)


account1 = BankAccount("Jagadeesh", 50000)

account1.deposit(5000)
account1.withdraw(10000)
account1.display_balance()

class Mobile:
    def __init__(self, brand, model, price):
        self.brand = brand
        self.model = model
        self.price = price

    def display(self):
        print("Brand:", self.brand)
        print("Model:", self.model)
        print("Price:", self.price)
        print()


mobile1 = Mobile("Samsung", "S24", 70000)
mobile2 = Mobile("Apple", "iPhone 15", 80000)
mobile3 = Mobile("OnePlus", "12", 60000)

mobile1.display()
mobile2.display()
mobile3.display()

class Rectangle:
    def __init__(self, length, breadth):
        self.length = length
        self.breadth = breadth

    def area(self):
        print("Area:", self.length * self.breadth)

    def perimeter(self):
        print("Perimeter:", 2 * (self.length + self.breadth))


rectangle1 = Rectangle(10, 5)

rectangle1.area()
rectangle1.perimeter()

class Student:
    def __init__(self, name, marks):
        self.name = name
        self.marks = marks

    def display_marks(self):
        print("Name:", self.name)
        print("Marks:", self.marks)

    def check_result(self):
        if self.marks >= 40:
            print("Result: Pass")
        else:
            print("Result: Fail")

        print()


student1 = Student("Rahul", 75)
student2 = Student("Aparna", 35)
student3 = Student("Kiran", 60)
student4 = Student("Priya", 25)
student5 = Student("Arun", 90)

student1.display_marks()
student1.check_result()

student2.display_marks()
student2.check_result()

student3.display_marks()
student3.check_result()

student4.display_marks()
student4.check_result()

student5.display_marks()
student5.check_result()

class Employee:
    def __init__(self, name, salary):
        self.name = name
        self.salary = salary

    def calculate_bonus(self):
        if self.salary >= 50000:
            bonus = self.salary * 10 / 100
        else:
            bonus = self.salary * 5 / 100

        total_salary = self.salary + bonus

        print("Employee Name:", self.name)
        print("Salary:", self.salary)
        print("Bonus:", bonus)
        print("Total Salary:", total_salary)
        print()


employee1 = Employee("Aparna", 60000)
employee2 = Employee("Rahul", 40000)

employee1.calculate_bonus()
employee2.calculate_bonus()

class Product:
    def __init__(self, product_name, price):
        self.product_name = product_name
        self.price = price

    def calculate_discount(self):
        if self.price >= 5000:
            discount = self.price * 20 / 100
        elif self.price >= 2000:
            discount = self.price * 10 / 100
        else:
            discount = self.price * 5 / 100

        final_price = self.price - discount

        print("Product:", self.product_name)
        print("Original Price:", self.price)
        print("Discount:", discount)
        print("Final Price:", final_price)
        print()


product1 = Product("Laptop", 60000)
product2 = Product("Headphones", 3000)
product3 = Product("Mouse", 1000)

product1.calculate_discount()
product2.calculate_discount()
product3.calculate_discount()

class ATM:
    def __init__(self, account_number, balance):
        self.account_number = account_number
        self.balance = balance

    def deposit(self, amount):
        self.balance = self.balance + amount
        print("Deposited:", amount)

    def withdraw(self, amount):
        if amount > self.balance:
            print("Insufficient Balance")
        else:
            self.balance = self.balance - amount
            print("Withdrawn:", amount)

    def check_balance(self):
        print("Current Balance:", self.balance)


atm1 = ATM("123456789", 50000)

atm1.check_balance()
atm1.deposit(10000)
atm1.check_balance()
atm1.withdraw(15000)
atm1.check_balance()

class Car:
    def __init__(self, brand, model, price, fuel_type):
        self.brand = brand
        self.model = model
        self.price = price
        self.fuel_type = fuel_type

    def display(self):
        print("Brand:", self.brand)
        print("Model:", self.model)
        print("Price:", self.price)
        print("Fuel Type:", self.fuel_type)

    def check_price(self):
        if self.price > 1000000:
            print("Premium Car")
        else:
            print("Normal Car")


car1 = Car("Toyota", "Fortuner", 4000000, "Diesel")

car1.display()
car1.check_price()

class ElectricityBill:
    def __init__(self, customer_name, units):
        self.customer_name = customer_name
        self.units = units

    def calculate_bill(self):
        if self.units <= 100:
            self.bill = self.units * 2
        elif self.units <= 200:
            self.bill = self.units * 3
        elif self.units <= 300:
            self.bill = self.units * 5
        else:
            self.bill = self.units * 7

    def display_bill(self):
        print("Customer Name:", self.customer_name)
        print("Units:", self.units)
        print("Electricity Bill:", self.bill)


customer1 = ElectricityBill("Jagadeesh", 250)

customer1.calculate_bill()
customer1.display_bill()

class Book:
    def __init__(self, title, author, price, available):
        self.title = title
        self.author = author
        self.price = price
        self.available = available

    def display_book(self):
        print("Title:", self.title)
        print("Author:", self.author)
        print("Price:", self.price)
        print("Available:", self.available)

    def borrow_book(self):
        if self.available:
            self.available = False
            print("Book borrowed successfully")
        else:
            print("Book is not available")

    def return_book(self):
        self.available = True
        print("Book returned successfully")


book1 = Book("Python Programming", "John", 500, True)

book1.display_book()

book1.borrow_book()

book1.display_book()

book1.return_book()

book1.display_book()

class Product:
    def __init__(self, name, price, quantity):
        self.name = name
        self.price = price
        self.quantity = quantity

    def calculate_total(self):
        return self.price * self.quantity

    def display_product(self):
        print("Product:", self.name)
        print("Price:", self.price)
        print("Quantity:", self.quantity)
        print("Total:", self.calculate_total())
        print()


product1 = Product("Laptop", 50000, 1)
product2 = Product("Mouse", 1000, 2)
product3 = Product("Keyboard", 2000, 1)

product1.display_product()
product2.display_product()
product3.display_product()

total = (
    product1.calculate_total()
    + product2.calculate_total()
    + product3.calculate_total()
)

print("Total Shopping Amount:", total)

class Employee:
    def __init__(self, name, salary, rating):
        self.name = name
        self.salary = salary
        self.rating = rating

    def display(self):
        print("Name:", self.name)
        print("Salary:", self.salary)
        print("Rating:", self.rating)

    def calculate_increment(self):
        if self.rating >= 4.5:
            increment = self.salary * 20 / 100
        elif self.rating >= 3.5:
            increment = self.salary * 10 / 100
        else:
            increment = self.salary * 5 / 100

        print("Increment:", increment)
        print("New Salary:", self.salary + increment)
        print()


employee1 = Employee("Aparna", 60000, 4.7)
employee2 = Employee("Rahul", 50000, 4.0)
employee3 = Employee("Kiran", 40000, 3.0)

employee1.display()
employee1.calculate_increment()

employee2.display()
employee2.calculate_increment()

employee3.display()
employee3.calculate_increment()

class BankAccount:
    def __init__(self, account_holder, balance):
        self.account_holder = account_holder
        self.balance = balance

    def deposit(self, amount):
        self.balance = self.balance + amount
        print("Deposited:", amount)

    def withdraw(self, amount):
        if self.balance - amount < 1000:
            print("Withdrawal not allowed")
            print("Minimum balance of ₹1000 must be maintained")
        else:
            self.balance = self.balance - amount
            print("Withdrawn:", amount)

    def check_balance(self):
        print("Account Holder:", self.account_holder)
        print("Balance:", self.balance)


account1 = BankAccount("Jagadeesh", 5000)

account1.check_balance()

account1.withdraw(3000)
account1.check_balance()

account1.withdraw(1500)
account1.check_balance()

class FoodOrder:
    def __init__(self, customer_name, food_name, price, quantity):
        self.customer_name = customer_name
        self.food_name = food_name
        self.price = price
        self.quantity = quantity

    def calculate_total(self):
        return self.price * self.quantity

    def apply_discount(self):
        total = self.calculate_total()

        if total >= 2000:
            discount = total * 20 / 100
        elif total >= 1000:
            discount = total * 10 / 100
        else:
            discount = 0

        return discount

    def display_order(self):
        total = self.calculate_total()
        discount = self.apply_discount()
        final_price = total - discount

        print("Customer Name:", self.customer_name)
        print("Food:", self.food_name)
        print("Price:", self.price)
        print("Quantity:", self.quantity)
        print("Total:", total)
        print("Discount:", discount)
        print("Final Price:", final_price)


order1 = FoodOrder("Jagadeesh", "Biryani", 500, 4)

order1.display_order()

class Patient:
    def __init__(self, name, age, disease, bill):
        self.name = name
        self.age = age
        self.disease = disease
        self.bill = bill

    def display_patient(self):
        print("Name:", self.name)
        print("Age:", self.age)
        print("Disease:", self.disease)
        print("Bill:", self.bill)

    def add_bill(self, amount):
        self.bill = self.bill + amount
        print("Bill updated")

    def check_bill(self):
        print("Current Bill:", self.bill)


patient1 = Patient("Rahul", 30, "Fever", 5000)
patient2 = Patient("Aparna", 25, "Infection", 7000)

patient1.display_patient()
patient1.add_bill(2000)
patient1.check_bill()

print()

patient2.display_patient()
patient2.add_bill(3000)
patient2.check_bill()

class Employee:
    def __init__(self, name, total_days, present_days):
        self.name = name
        self.total_days = total_days
        self.present_days = present_days

    def attendance_percentage(self):
        percentage = (self.present_days / self.total_days) * 100
        print("Attendance:", percentage, "%")

    def check_attendance(self):
        percentage = (self.present_days / self.total_days) * 100

        if percentage >= 75:
            print("Eligible")
        else:
            print("Not Eligible")


employee1 = Employee("Aparna", 100, 85)
employee2 = Employee("Rahul", 100, 60)

employee1.attendance_percentage()
employee1.check_attendance()

print()

employee2.attendance_percentage()
employee2.check_attendance()

class MovieTicket:
    def __init__(self, movie_name, ticket_price, number_of_tickets):
        self.movie_name = movie_name
        self.ticket_price = ticket_price
        self.number_of_tickets = number_of_tickets

    def calculate_total(self):
        return self.ticket_price * self.number_of_tickets

    def apply_discount(self):
        total = self.calculate_total()

        if self.number_of_tickets >= 5:
            discount = total * 10 / 100
        else:
            discount = 0

        return discount

    def display_ticket(self):
        total = self.calculate_total()
        discount = self.apply_discount()
        final_price = total - discount

        print("Movie:", self.movie_name)
        print("Ticket Price:", self.ticket_price)
        print("Number of Tickets:", self.number_of_tickets)
        print("Total:", total)
        print("Discount:", discount)
        print("Final Price:", final_price)


ticket1 = MovieTicket("Avengers", 300, 5)

ticket1.display_ticket()

class Student:
    def __init__(self, name, roll_no, python, sql, powerbi):
        self.name = name
        self.roll_no = roll_no
        self.python = python
        self.sql = sql
        self.powerbi = powerbi

    def calculate_total(self):
        return self.python + self.sql + self.powerbi

    def calculate_average(self):
        total = self.calculate_total()
        return total / 3

    def calculate_grade(self):
        average = self.calculate_average()

        if average >= 90:
            return "A"
        elif average >= 75:
            return "B"
        elif average >= 60:
            return "C"
        elif average >= 40:
            return "D"
        else:
            return "Fail"

    def display_report(self):
        print("Student Name:", self.name)
        print("Roll No:", self.roll_no)
        print("Python:", self.python)
        print("SQL:", self.sql)
        print("Power BI:", self.powerbi)
        print("Total:", self.calculate_total())
        print("Average:", self.calculate_average())
        print("Grade:", self.calculate_grade())


student1 = Student("Jagadeesh", 101, 90, 85, 95)

student1.display_report()
