# Write a function calculate_bill(units) that returns the electricity bill based on the rules: 0–100 units → ₹2 per unit 101–200 units → ₹3 per unit Above 200 units → ₹5 per unit Call the function and display the bill.
import datetime
import string
import math
import random


def calculate_bill(units):
    if units <= 100:
        bill = units * 2
    elif units <= 200:
        bill = (100 * 2) + (units - 100) * 3
    else:
        bill = (100 * 2) + (100 * 3) + (units - 200) * 5
    return bill


units = int(input("Enter the number of units consumed: "))
bill_amount = calculate_bill(units)
print(f"Total electricity bill for {units} units is: ₹{bill_amount}")
print("\n")

# Write a function student_details(name, branch="CSE", year=2) and print student information using: Positional arguments Keyword arguments Default arguments


def student_details(name, branch="CSE", year=2):
    print(f"Name: {name}")
    print(f"Branch: {branch}")
    print(f"Year: {year}")


student_details("Alice", "ECE", 3)  # Positional arguments
student_details("Charlie", "CSE", 4)  # Keyword arguments
student_details("David", "Allied health science", 2)  # Default arguments
student_details(name="Bob", year=1)  # Keyword arguments
# Default arguments
print("\n")

# Create a function *average_marks(marks) to compute and return the average of any number of marks passed to it.


def average_marks(*marks):
    total = sum(marks)
    average = total / len(marks)
    return average


avg = average_marks(85, 90, 78, 92, 88)
print(f"The average marks are: {avg}")
print("\n")

# Given a list of integers, use lambda and map() to generate a new list where each number is replaced by its cube.
numbers = [1, 2, 3, 4, 5]
cubes = list(map(lambda x: x**3, numbers))
print(f"The cubes of the numbers are: {cubes}")
print("\n")

# Using lambda and filter(), print all numbers between 1 and 100 that are divisible by 7.
divisible_by_7 = list(filter(lambda x: x % 7 == 0, range(1, 101)))
print(f"Numbers between 1 and 100 divisible by 7: {divisible_by_7}")
print("\n")

# Write a program to generate: A 6-digit OTP using the random module Today’s date in dd/mm/yyyy format using the datetime module Square root of a number using the math module
otp = ''.join([str(random.randint(0, 9)) for _ in range(6)])
print(f"Generated 6-digit OTP: {otp}")
today_date = datetime.datetime.now().strftime("%d/%m/%Y")
print(f"Today's date: {today_date}")
number = int(input("Enter a number to find its square root: "))
sqrt_number = math.sqrt(number)
print(f"Square root of {number} is: {sqrt_number}")
print("\n")

# Create a module operations.py with: add(a,b) subtract(a,b) multiply(a,b) divide(a,b) Import this module into another Python file and perform all operations.


def add(a, b):
    return a + b


def subtract(a, b):
    return a - b


def multiply(a, b):
    return a * b


def divide(a, b):
    if b != 0:
        return a / b
    else:
        return "Error! Division by zero."


print("\n")

# Create a custom module studentutils.py with functions: full_name(first, last) get_attendance(total, attended) eligibility(attendance_percentage) Import the module in main.py and test with sample data.


def full_name(first, last):
    return f"{first} {last}"


def get_attendance(total, attended):
    return (attended / total) * 100


def eligibility(attendance_percentage):
    return attendance_percentage >= 75


print("\n")

# Personal Password Generator -Use built-in modules + lambda to: -Generate random strong passwords -Allow user to choose length & character type -Save password to a local text file -Use a custom module for password generation function


def generate_password(length, use_special_chars):
    characters = string.ascii_letters + string.digits
    if use_special_chars:
        characters += string.punctuation
    password = ''.join(random.choice(characters) for _ in range(length))
    return password


length = int(input("Enter desired password length: "))
use_special_chars = input("Include special characters? (y/n): ").lower() == 'y'
password = generate_password(length, use_special_chars)
print(f"Generated Password: {password}")
with open("passwords.txt", "a") as file:
    file.write(password + "\n")
print("Password saved to passwords.txt")
