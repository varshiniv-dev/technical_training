# Write the python program to check whether given number is positive , negative or zero.
num = float(input("Enter a number: "))
if num > 0:
    print("The number is positive.")
elif num < 0:
    print("The number is negative.")
else:
    print("The number is zero.")
print("\n")

# Write a python program to check the number given from user whether  it is even or odd
num = int(input("Enter an integer: "))
if num % 2 == 0:
    print("The number is even.")
else:
    print("The number is odd.")
print("\n")

# Take 2 numbers as a input and print the larger one using an if else statement.
num1 = float(input("Enter first number: "))
num2 = float(input("Enter second number: "))
if num1 > num2:
    print(f"The larger number is {num1}.")
else:
    print(f"The larger number is {num2}.")
print("\n")

# Write a program to check whether a person is eligible to vote based on their age
age = int(input("Enter your age: "))
if age >= 18:
    print("You are eligible to vote.")
else:
    print("You are not eligible to vote.")
print("\n")

# Write a program to accept the temperature in Celsius  and display message like - cold day for<=15`C - pleasant for 16-30`C - hot day for >30`C
temp_celsius = float(input("Enter temperature in Celsius: "))
if temp_celsius <= 15:
    print("Cold day")
elif 16 <= temp_celsius <= 30:
    print("Pleasant day")
else:
    print("Hot day")
print("\n")

# Write a python program that accept the marks from the user and assign per grade as per the follow -90 above-A+ -80-89-A -70-79-B -60-69-C -below 60-fail
marks = float(input("Enter your marks: "))
if marks >= 90:
    grade = "A+"
elif 80 <= marks < 90:
    grade = "A"
elif 70 <= marks < 80:
    grade = "B"
elif 60 <= marks < 70:
    grade = "C"
else:
    grade = "Fail"
print(f"Your grade is: {grade}")
print("\n")

# Write the program to determine whether the given year is a leap year or not by using conditional statements
year = int(input("Enter a year: "))
if (year % 4 == 0 and year % 100 != 0) or (year % 400 == 0):
    print(f"{year} is a leap year.")
else:
    print(f"{year} is not a leap year.")
print("\n")

# write a program to design a discount calculator on below condition a shop gives a 10%discount a purchases above 1000rs and 20 % discount  a purchases above 5000rs calculate the final  price after discount
purchase_amount = float(input("Enter the purchase amount: "))
if purchase_amount > 5000:
    discount = 0.20 * purchase_amount
elif purchase_amount > 1000:
    discount = 0.10 * purchase_amount
else:
    discount = 0
final_price = purchase_amount - discount
print(f"Discount applied: {discount}")
print(f"Final price after discount: {final_price}")
print("\n")

#
