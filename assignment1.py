# Write a python program to display your name, Department, college name, using three different print statement.
print("Name: John Doe")
print("Department: Computer Science")
print("College Name: ABC University")
print("\n")

# Write a program that ask a user for their name and prints  (hello *name* hello world!)
name = input("Enter your name: ")
print(f"Hello {name}, Hello World!")
print("\n")

# Write a program to take 2 numbers as input from the user and display their sum.
num1 = float(input("Enter first number: "))
num2 = float(input("Enter second number: "))
sum = num1 + num2
print(f"The sum of {num1} and {num2} is {sum}")
print("\n")

# Write a python script that prints three lines about why python is your favorite programming language.
print("Python is my favorite programming language because:")
print("1. It has a simple and easy-to-read syntax.")
print("2. It has a large and supportive community.")
print("3. It is versatile and can be used for various applications like web development, data science, and automation.")
print("\n")

# Write a program to perform addition subtraction multiplication and division on two numbers entered by the user.
num1 = float(input("Enter first number: "))
num2 = float(input("Enter second number: "))
addition = num1 + num2
subtraction = num1 - num2
multiplication = num1 * num2
division = num1 / num2 if num2 != 0 else "undefined (cannot divide by zero)"
print(f"Addition: {addition}")
print(f"Subtraction: {subtraction}")
print(f"Multiplication: {multiplication}")
print(f"Division: {division}")
