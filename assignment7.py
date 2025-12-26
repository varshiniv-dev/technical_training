# Write a program to demonstrate single inheritance using classes: Class Animal → method eat() Class Dog → method bark()
import math


class Animal:
    def eat(self):
        return "The animal is eating."


class Dog(Animal):
    def bark(self):
        return "The dog is barking."


# Create an instance of Dog
dog = Dog()
# Call methods from both classes
print(dog.eat())  # Inherited from Animal
print(dog.bark())  # From Dog class
print("Single inheritance demonstration complete.")
print("\n")

# Create a program to show multilevel inheritance using classes: Each class should contain one unique method


class Grandparent:
    def grandparent_method(self):
        return "This is the grandparent method."


class Parent(Grandparent):
    def parent_method(self):
        return "This is the parent method."


class Child(Parent):
    def child_method(self):
        return "This is the child method."


# Create an instance of Child
child = Child()
# Call methods from all three classes
print(child.grandparent_method())  # From Grandparent class
print(child.parent_method())       # From Parent class
print(child.child_method())        # From Child class
print("Multilevel inheritance demonstration complete.")
print("\n")

# Create a program to show multilevel inheritance using classes: Person → Student → CollegeStudent Each class should contain one unique method.


class Person:
    def person_info(self):
        return "This is the person information."


class Student(Person):
    def student_info(self):
        return "This is the student information."


class CollegeStudent(Student):
    def college_student_info(self):
        return "This is the college student information."


# Create an instance of CollegeStudent
college_student = CollegeStudent()
# Call methods from all three classes
print(college_student.person_info())          # From Person class
print(college_student.student_info())         # From Student class
print(college_student.college_student_info())  # From CollegeStudent class
print("Multilevel inheritance demonstration complete.")
print("\n")

# Write a program to illustrate method overriding using: Class Bird (method fly()) Class Penguin overrides fly().


class Bird:
    def fly(self):
        return "The bird is flying."


class Penguin(Bird):
    def fly(self):
        return "Penguins cannot fly."


# Create an instance of Penguin
penguin = Penguin()
# Call the overridden method
print(penguin.fly())  # Calls the overridden method in Penguin
print("Method overriding demonstration complete.")
print("\n")

# Write a program to implement polymorphism using a common method name area() for: Class Circle Class Square Class Rectangle Each class should compute its own area.


class Circle:
    def __init__(self, radius):
        self.radius = radius

    def area(self):
        return math.pi * (self.radius ** 2)


class Square:
    def __init__(self, side):
        self.side = side

    def area(self):
        return self.side ** 2


class Rectangle:
    def __init__(self, length, width):
        self.length = length
        self.width = width

    def area(self):
        return self.length * self.width


# Create instances of each shape
circle = Circle(5)
square = Square(4)
rectangle = Rectangle(3, 6)
# Call the area method for each shape
print(f"Area of Circle: {circle.area()}")
print(f"Area of Square: {square.area()}")
print(f"Area of Rectangle: {rectangle.area()}")
print("Polymorphism demonstration complete.")
print("\n")

# Create a parent class Vehicle and a child class Car. Use constructor in both classes. Use super() to call parent constructor. Add a method to display details of both classes.


class Vehicle:
    def __init__(self, make, model):
        self.make = make
        self.model = model

    def vehicle_info(self):
        return f"Vehicle Make: {self.make}, Model: {self.model}"


class Car(Vehicle):
    def __init__(self, make, model, year):
        super().__init__(make, model)
        self.year = year

    def car_info(self):
        return f"Car Year: {self.year}, " + self.vehicle_info()


# Create an instance of Car
car1 = Car("Porschw", "911", 2020)
car2 = Car("BMW", "M5", 2019)
car3 = Car("Audi", "R8", 2021)
car4 = Car("Mercedes", "C-Class", 2018)
# Display details of the cars
print(car1.car_info())
print(car2.car_info())
print(car3.car_info())
print(car4.car_info())
print("Constructor and super() demonstration complete.")
print("\n")

# Student Management SystemCreate a Student class with name, roll, marks.Add methods: display(), grade()Accept details for 5 students and:Display allFind highest marksDisplay topper details


class Student:
    def __init__(self, name, roll, marks):
        self.name = name
        self.roll = roll
        self.marks = marks

    def display(self):
        return f"Name: {self.name}, Roll: {self.roll}, Marks: {self.marks}"

    def grade(self):
        if self.marks >= 90:
            return "A"
        elif self.marks >= 80:
            return "B"
        elif self.marks >= 70:
            return "C"
        elif self.marks >= 60:
            return "D"
        else:
            return "F"


# Accept details for 5 students
students = []
for i in range(5):
    name = input(f"Enter name of student {i+1}: ")
    roll = input(f"Enter roll number of student {i+1}: ")
    marks = float(input(f"Enter marks of student {i+1}: "))
    students.append(Student(name, roll, marks))
# Display all students
print("\nStudent Details:")
for student in students:
    print(student.display(), f"Grade: {student.grade()}")
# Find highest marks and topper details
topper = max(students, key=lambda s: s.marks)
print("\nTopper Details:")
print(topper.display(), f"Grade: {topper.grade()}")
print("Student Management System demonstration complete.")
# Single Inheritance Demonstration Complete
print("\n")
# Multilevel Inheritance Demonstration Complete

# Create a class BankAccount with: deposit(), withdraw(), check_balance() methods Initialize balance through constructor Perform operations for multiple users


class BankAccount:
    def __init__(self, initial_balance=0):
        self.balance = initial_balance

    def deposit(self, amount):
        self.balance += amount
        return f"Deposited: {amount}. New Balance: {self.balance}"

    def withdraw(self, amount):
        if amount > self.balance:
            return "Insufficient funds."
        self.balance -= amount
        return f"Withdrew: {amount}. New Balance: {self.balance}"

    def check_balance(self):
        return f"Current Balance: {self.balance}"


# Create accounts for multiple users
user1 = BankAccount(1000)
user2 = BankAccount(500)
# Perform operations for user1
print(user1.deposit(200))
print(user1.withdraw(150))
print(user1.check_balance())
# Perform operations for user2
print(user2.deposit(300))
print(user2.withdraw(800))  # Should show insufficient funds
print(user2.check_balance())
print("Bank Account demonstration complete.")
#!/usr/bin/env python3
print("\n")
# Bank Account Demonstration Complete

# Create a Library System using classes: Book (title, author, ISBN) Library (list of books) Methods: add_book(), search_book(), display_books()


class Book:
    def __init__(self, title, author, isbn):
        self.title = title
        self.author = author
        self.isbn = isbn

    def __str__(self):
        return f"Title: {self.title}, Author: {self.author}, ISBN: {self.isbn}"


class Library:
    def __init__(self):
        self.books = []

    def add_book(self, book):
        self.books.append(book)
        return f"Book '{book.title}' added to the library."

    def search_book(self, title):
        for book in self.books:
            if book.title.lower() == title.lower():
                return str(book)
        return "Book not found."

    def display_books(self):
        if not self.books:
            return "No books in the library."
        return "\n".join(str(book) for book in self.books)


# Create a library instance
library = Library()
# Add books to the library
library.add_book(Book("Edge of darkness trilogy",
                 "Leigh Rivers", "9780345446781"))
library.add_book(Book("Twisted series", "Ana Huang", "9780451524935"))
library.add_book(Book("Shatter me series", "Tahereh Mafi", "9781250301697"))
library.add_book(Book("Campus games", "Stephanie Alves", "9780735219106"))
# Display all books
print("\nAll Books in the Library:")
print(library.display_books())
find_book = "Twisted series"
if find_book:
    print(f"\nSearching for book: {find_book}")
    print(library.search_book(find_book))
print("Library System demonstration complete.")
print("\n")
# Library System Demonstration Complete

# Build an E-commerce Product SystemClass Product → id, name, price Class Electronics inherits Product → warranty Class Clothing inherits Product → size Demonstrate inheritance & polymorphism.


class Product:
    def __init__(self, product_id, name, price):
        self.product_id = product_id
        self.name = name
        self.price = price

    def product_info(self):
        return f"ID: {self.product_id}, Name: {self.name}, Price: {self.price}"


class Electronics(Product):
    def __init__(self, product_id, name, price, warranty):
        super().__init__(product_id, name, price)
        self.warranty = warranty

    def product_info(self):
        base_info = super().product_info()
        return f"{base_info}, Warranty: {self.warranty} years"


class Clothing(Product):
    def __init__(self, product_id, name, price, size):
        super().__init__(product_id, name, price)
        self.size = size

    def product_info(self):
        base_info = super().product_info()
        return f"{base_info}, Size: {self.size}"


# Create instances of Electronics and Clothing
laptop = Electronics(101, "Laptop", 1200.00, 2)
tshirt = Clothing(202, "T-Shirt", 25.00, "M")
# Display product information
print("Product Information:")
print(laptop.product_info())
print(tshirt.product_info())
print("E-commerce Product System demonstration complete.")
print("\n")
# E-commerce Product System Demonstration Complete

# Create a program using composition: Class Engine Class Car containing Engine object Show how both classes interact


class Engine:
    def __init__(self, horsepower, type):
        self.horsepower = horsepower
        self.type = type

    def engine_info(self):
        return f"Engine Type: {self.type}, Horsepower: {self.horsepower} HP"


class Car:
    def __init__(self, make, model, engine):
        self.make = make
        self.model = model
        self.engine = engine  # Composition: Car has an Engine

    def car_info(self):
        engine_details = self.engine.engine_info()
        return f"Car Make: {self.make}, Model: {self.model}, {engine_details}"


# Create an Engine instance
engine1 = Engine(300, "V6")
# Create a Car instance with the Engine
car = Car("Ford", "Mustang", engine1)
# Display car information including engine details
print("Car Information:")
print(car.car_info())
print("Composition demonstration complete.")
print("\n")
# Composition Demonstration Complete

# Create a College Attendance System using OOP with:  Student class Attendance class Methods to add, update, and display attendance


class Student:
    def __init__(self, student_id, name):
        self.student_id = student_id
        self.name = name

    def student_info(self):
        return f"ID: {self.student_id}, Name: {self.name}"


class Attendance:
    def __init__(self):
        self.attendance_record = {}

    def add_attendance(self, student, date, status):
        if student.student_id not in self.attendance_record:
            self.attendance_record[student.student_id] = []
        self.attendance_record[student.student_id].append((date, status))

    def update_attendance(self, student, date, status):
        if student.student_id in self.attendance_record:
            for i, (d, s) in enumerate(self.attendance_record[student.student_id]):
                if d == date:
                    self.attendance_record[student.student_id][i] = (
                        date, status)
                    return "Attendance updated."
        return "Attendance record not found."

    def display_attendance(self, student):
        if student.student_id in self.attendance_record:
            records = self.attendance_record[student.student_id]
            return f"Attendance for {student.name}:\n" + "\n".join(f"{date}: {status}" for date, status in records)
        return "No attendance records found."


# Create Student instances
student1 = Student(1, "Ansh")
student2 = Student(2, "Veer")
# Create Attendance instance
attendance = Attendance()
# Add attendance records
attendance.add_attendance(student1, "2024-09-01", "Present")
attendance.add_attendance(student1, "2024-09-02", "Absent")
attendance.add_attendance(student2, "2024-09-01", "Present")
# Update an attendance record
attendance.update_attendance(student1, "2024-09-02", "Present")
# Display attendance records
print(attendance.display_attendance(student1))
print(attendance.display_attendance(student2))
print("College Attendance System demonstration complete.")
print("\n")

# Create a Bank ATM Simulation using: User Authentication Deposit, Withdraw, Transfer Show mini statement


class ATM:
    def __init__(self, user_id, pin, balance=0):
        self.user_id = user_id
        self.pin = pin
        self.balance = balance
        self.transaction_history = []

    def authenticate(self, input_pin):
        return self.pin == input_pin

    def deposit(self, amount):
        self.balance += amount
        self.transaction_history.append(f"Deposited: {amount}")
        return f"Deposited: {amount}. New Balance: {self.balance}"

    def withdraw(self, amount):
        if amount > self.balance:
            return "Insufficient funds."
        self.balance -= amount
        self.transaction_history.append(f"Withdrew: {amount}")
        return f"Withdrew: {amount}. New Balance: {self.balance}"

    def transfer(self, amount, recipient_atm):
        if amount > self.balance:
            return "Insufficient funds."
        self.balance -= amount
        recipient_atm.balance += amount
        self.transaction_history.append(
            f"Transferred: {amount} to User {recipient_atm.user_id}")
        return f"Transferred: {amount} to User {recipient_atm.user_id}. New Balance: {self.balance}"

    def mini_statement(self):
        return "Transaction History:\n" + "\n".join(self.transaction_history)


# Create ATM instances for two users
atm_user1 = ATM("user1", "1234", 1000)
atm_user2 = ATM("user2", "5678", 500)
# Authenticate user1
if atm_user1.authenticate("1234"):
    print(atm_user1.deposit(200))
    print(atm_user1.withdraw(150))
    print(atm_user1.transfer(300, atm_user2))
    print(atm_user1.mini_statement())
else:
    print("Authentication failed for User 1.")
# Authenticate user2
if atm_user2.authenticate("5678"):
    print(atm_user2.deposit(100))
    print(atm_user2.withdraw(50))
    print(atm_user2.mini_statement())
else:
    print("Authentication failed for User 2.")
print("Bank ATM Simulation demonstration complete.")
print("\n")

# Build a University Result Management System using: Base class Person Derived class Student Attributes: subject marks Methods: calculate total, percentage, grade


class Person:
    def __init__(self, name, age):
        self.name = name
        self.age = age

    def person_info(self):
        return f"Name: {self.name}, Age: {self.age}"


class Student(Person):
    def __init__(self, name, age, marks):
        super().__init__(name, age)
        self.marks = marks  # marks is a dictionary of subject: score

    def calculate_total(self):
        return sum(self.marks.values())

    def calculate_percentage(self):
        total_marks = self.calculate_total()
        # Assuming each subject is out of 100
        return (total_marks / (len(self.marks) * 100)) * 100

    def grade(self):
        percentage = self.calculate_percentage()
        if percentage >= 90:
            return "A"
        elif percentage >= 80:
            return "B"
        elif percentage >= 70:
            return "C"
        elif percentage >= 60:
            return "D"
        else:
            return "F"


# Create a Student instance
student = Student("Riya", 20, {"Math": 95, "Science":
                               88, "History": 76, "English": 84})
# Display student information and results
print(student.person_info())
print(f"Total Marks: {student.calculate_total()}")
print(f"Percentage: {student.calculate_percentage():.2f}%")
print(f"Grade: {student.grade()}")
print("University Result Management System demonstration complete.")
print("\n")
# University Result Management System Demonstration Complete

# Create a Hospital Management Model using classes: Patient, Doctor, Appointment Demonstrate constructor, inheritance, polymorphism


class Person:
    def __init__(self, name, age):
        self.name = name
        self.age = age

    def person_info(self):
        return f"Name: {self.name}, Age: {self.age}"


class Patient(Person):
    def __init__(self, name, age, ailment):
        super().__init__(name, age)
        self.ailment = ailment

    def patient_info(self):
        base_info = self.person_info()
        return f"{base_info}, Ailment: {self.ailment}"


class Doctor(Person):
    def __init__(self, name, age, specialty):
        super().__init__(name, age)
        self.specialty = specialty

    def doctor_info(self):
        base_info = self.person_info()
        return f"{base_info}, Specialty: {self.specialty}"


class Appointment:
    def __init__(self, patient, doctor, date):
        self.patient = patient
        self.doctor = doctor
        self.date = date

    def appointment_info(self):
        return f"Appointment on {self.date}:\nPatient: {self.patient.patient_info()}\nDoctor: {self.doctor.doctor_info()}"


# Create instances of Patient and Doctor
patient1 = Patient("Aarav", 30, "Flu")
doctor1 = Doctor("Dr. Mehta", 45, "General Physician")
# Create an Appointment instance
appointment1 = Appointment(patient1, doctor1, "2024-10-15")
# Display appointment information
print(appointment1.appointment_info())
print("Hospital Management Model demonstration complete.")
print("\n")
# Hospital Management Model Demonstration Complete

# Create a Transport Booking System with: Base class Vehicle Derived classes Bus, Auto, Taxi Include fare calculation method (polymorphism)


class Vehicle:
    def __init__(self, vehicle_number):
        self.vehicle_number = vehicle_number

    def fare(self):
        raise NotImplementedError("Subclasses must implement this method.")


class Bus(Vehicle):
    def fare(self):
        return 50  # Fixed fare for bus


class Auto(Vehicle):
    def fare(self):
        return 30  # Fixed fare for auto


class Taxi(Vehicle):
    def fare(self):
        return 100  # Fixed fare for taxi


# Create instances of each vehicle type
bus1 = Bus("BUS123")
auto1 = Auto("AUTO456")
taxi1 = Taxi("TAXI789")
# Display fare for each vehicle
print(f"Bus Fare: {bus1.fare()}")
print(f"Auto Fare: {auto1.fare()}")
print(f"Taxi Fare: {taxi1.fare()}")
print("Transport Booking System demonstration complete.")

# or


class vehicle:
    def __init__(self, distance):
        self.distance = distance

    def fare(self):
        pass


class bus(vehicle):
    def fare(self):
        return self.distance*5


class auto(vehicle):
    def fare(self):
        return self.distance*7


class taxi(vehicle):
    def fare(self):
        return self.distance*10


buslist = [bus(10), bus(20), bus(15)]
autolist = [auto(10), auto(20), auto(30)]
taxilist = [taxi(100), taxi(200), taxi(300)]
print("Bus fare for 10 km:", buslist[0].fare())
print("Auto fare for 10 km:", autolist[0].fare())
print("Taxi fare for 10 km:", taxilist[0].fare())
print("Transport Booking System demonstration complete.")
print("\n")
