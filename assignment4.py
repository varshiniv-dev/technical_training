# Write a program to calculate the factorial of a number using a while loop.
num = int(input("Enter a number to calculate its factorial: "))
factorial = 1
i = 1
while i <= num:
    factorial *= i
    i += 1
print(f"The factorial of {num} is {factorial}")
print("\n")

# write a program that counts thedigits in a given number using loops.
number = int(input("Enter a number to count its digits: "))
count = 0
while number != 0:
    number //= 10
    count += 1
print(f"The number of digits is: {count}")
print("\n")

# write a program to reverse a number using a loop
num = int(input("Enter a number to reverse: "))
reversed_num = 0
while num > 0:
    digit = num % 10
    reversed_num = reversed_num * 10 + digit
    num //= 10
print(f"The reversed number is: {reversed_num}")
print("\n")

# Demonstrate the use of pass statement inside a loop with an example.
for i in range(5):
    if i == 3:
        pass  # Placeholder for future code
    else:
        print(i)
        print("looping...")
print("looping complete")
print("\n")

# print a square pattern (5x5) of numbers
for i in range(1, 6):
    for j in range(1, 6):
        print(j, end=' ')
    print()
print("\n")

# write a program that prints all prime numbers between 1 and 100
for num in range(2, 101):
    is_prime = True
    for i in range(2, int(num**0.5) + 1):
        if num % i == 0:
            is_prime = False
            break
    if is_prime:
        print(num, end=' ')
print("\n")

# Write a program to check whether a given number is a palindrome or not (using loops).
num = int(input("Enter a number to check if it's a palindrome: "))
original_num = num
reversed_num = 0
while num > 0:
    digit = num % 10
    reversed_num = reversed_num * 10 + digit
    num //= 10
if original_num == reversed_num:
    print(f"{original_num} is a palindrome.")
else:
    print(f"{original_num} is not a palindrome.")
print("\n")

# Display the Fibonacci series up to n terms using a while loop.
n = int(input("Enter the number of terms for Fibonacci series: "))
a, b = 0, 1
count = 0
while count < n:
    print(a, end=' ')
    a, b = b, a + b
    count += 1
print("\n")

# Write a program that keeps taking input until the user enters “exit”.
while True:
    user_input = input("Enter something (type 'exit' to quit): ")
    if user_input.lower() == 'exit':
        break
    print(f"You entered: {user_input}")
print("\n")

# print a pyramid of stars
n = int(input("Enter the number of rows for the pyramid: "))
for i in range(1, n+1):
    print(' ' * (n - i) + '* ' * i)
print("\n")

# print a pyramid of stars in reverse order
n = int(input("Enter the number of rows for the reverse pyramid: "))
for i in range(n, 0, -1):
    print(' ' * (n - i) + '* ' * i)
print("\n")
