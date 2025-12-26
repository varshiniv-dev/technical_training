# Write a Python program that stores 5 subject marks in a list, converts it to a tuple, and displays the maximum and minimum marks
marks_list = []
for i in range(5):
    mark = float(input(f"Enter marks for subject {i+1}: "))
    marks_list.append(mark)
marks_tuple = tuple(marks_list)
max_mark = max(marks_tuple)
min_mark = min(marks_tuple)
print(f"Marks Tuple: {marks_tuple}")
print(f"Maximum marks: {max_mark}")
print(f"Minimum marks: {min_mark}")
print("\n")

# Maintain a list of (name, marks) pairs for 5 students using tuples inside a list, and display: -Student with highest marks -Student with lowest marks -Class average
students = []
for i in range(5):
    name = input(f"Enter name of student {i+1}: ")
    marks = float(input(f"Enter marks of {name}: "))
    students.append((name, marks))
highest_student = max(students, key=lambda x: x[1])
lowest_student = min(students, key=lambda x: x[1])
average_marks = sum(marks for name, marks in students) / len(students)
print(
    f"Student with highest marks: {highest_student[0]} ({highest_student[1]})")
print(f"Student with lowest marks: {lowest_student[0]} ({lowest_student[1]})")
print(f"Class average marks: {average_marks}")
print("\n")

# Create a list of 10 student names. - Print the list - Print the first, middle, and last element - Print the length of the list
student_names = []
for i in range(10):
    name = input(f"Enter name of student {i+1}: ")
    student_names.append(name)
print(f"Student Names List: {student_names}")
print(f"First Student: {student_names[0]}")
print(f"Middle Student: {student_names[len(student_names)//2]}")
print(f"Last Student: {student_names[-1]}")
print(f"Length of the list: {len(student_names)}")
print("\n")

# Given a list of student marks: -Perform the following:-Add a new mark at the end-Insert a mark at index 2-Remove the lowest mark-Sort the list in ascending order-Display the top 3 marks using slicing-Display all marks except the first and last
marks = [78, 85, 62, 90, 56, 89, 73, 95]
marks.append(88)
marks.insert(2, 77)
marks.remove(min(marks))
marks.sort()
print(f"Top 3 marks: {marks[-3:]}")
print(f"All marks except first and last: {marks[1:-1]}")
print("\n")

# Store the names of students and their marks in two separate lists. Sort the students according to marks (both lists should remain aligned) (Hint: Use zip()) Print the top 3 students with names
student_names = ["Alice", "Bob", "Charlie", "David", "Eve"]
student_marks = [85, 92, 78, 96, 88]
students = list(zip(student_names, student_marks))
students_sorted = sorted(students, key=lambda x: x[1], reverse=True)
print("Top 3 students with names:")
for i in range(min(3, len(students_sorted))):
    print(f"{students_sorted[i][0]} - {students_sorted[i][1]}")
print("\n")

# Write a menu-driven Python program using lists to: Add a student's mark Remove a student's mark Update a student's mark Display all marks Exit
marks = []
while True:
    print("Menu:")
    print("1. Add a student's mark")
    print("2. Remove a student's mark")
    print("3. Update a student's mark")
    print("4. Display all marks")
    print("5. Exit")
    choice = input("Enter your choice (1-5): ")
    if choice == '1':
        mark = float(input("Enter the mark to add: "))
        marks.append(mark)
        print("Mark added.")
    elif choice == '2':
        mark = float(input("Enter the mark to remove: "))
        if mark in marks:
            marks.remove(mark)
            print("Mark removed.")
        else:
            print("Mark not found.")
    elif choice == '3':
        old_mark = float(input("Enter the mark to update: "))
        if old_mark in marks:
            new_mark = float(input("Enter the new mark: "))
            index = marks.index(old_mark)
            marks[index] = new_mark
            print("Mark updated.")
        else:
            print("Mark not found.")
    elif choice == '4':
        print(f"All marks: {marks}")
    elif choice == '5':
        print("Exiting program.")
        break
    else:
        print("Invalid choice. Please try again.")
    print("\n")
