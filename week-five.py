# 3️⃣ Lambda Functions
#
# 🔹 What is a Lambda Function?
#
# A lambda function is a small, one-line anonymous function.


#🔍 When to Use Lambda?
#
# When you need a short function for a quick calculation.
#
# When using functions like map(), filter(), or sorted().
#
# ✅ Key Takeaways:
#
# ✔️ Use lambda for simple one-line functions.✔️ Syntax: lambda arguments: expression


# 4️⃣ Built-in Functions: map, filter, reduce
#
# 🔹 map()
#
# Applies a function to each item in an iterable.


def square(x):
    return x * x

numbers = [1, 2, 3, 4]
squared_numbers = list(map(square, numbers))
print(squared_numbers)  # Output: [1, 4, 9, 16]

# 🔹 filter()
#
# Filters elements based on a condition.

def is_even(n):
    return n % 2 == 0

numbers = [1, 2, 3, 4, 5, 6]
even_numbers = list(filter(is_even, numbers))
print(even_numbers)  # Output: [2, 4, 6]

# 🔹 reduce()
#
# Reduces an iterable to a single value.

from functools import reduce

def multiply(x, y):
    return x * y

numbers = [1, 2, 3, 4]
result = reduce(multiply, numbers)
print(result)  # Output: 24

# ✔️ map(function, iterable): Applies a function to all elements.
# ✔️ filter(function, iterable): Filters elements based on a condition.
# ✔️ reduce(function, iterable): Reduces elements to a single value.
#

# 📌 Project Title: Student Grade Management System
# 🔹 Description:
# This project will allow users to store, update, and analyze student grades using Python functions, control structures, and data structures like lists, tuples, and dictionaries.
#
# 🔨 Features to Implement
# 1️⃣ Add New Students and Their Grades
#
# Store student details in a dictionary (name, age, grades).
# Use functions to add and display students.
# 2️⃣ Calculate the Average Grade
#
# Use a function that takes a list of grades and returns the average.
# 3️⃣ Grade Analysis
#
# Determine the highest and lowest grades in the class.
# Use map(), filter(), and reduce() to analyze grades.
# 4️⃣ Search for a Student by Name
#
# Use a function to search if a student exists.
# 5️⃣ Update Student Grades
#
# Allow users to modify grades for a student.
# 6️⃣ Remove a Student
#
# Implement a function to delete a student from the system.
# 7️⃣ Report Generation
#
# Use list/dictionary comprehensions to summarize data quickly.
# 📌 Expected Concepts to Apply
# ✔ Lists & Tuples → Store multiple student grades.
# ✔ Dictionaries → Store student details (name, age, grades).
# ✔ Functions → For adding, updating, and removing students.
# ✔ Control Structures (if-else, loops) → To navigate the system.
# ✔ Lambda Functions → Quick calculations like doubling a grade.
# ✔ map(), filter(), reduce() → Data processing.
# ✔ List & Dictionary Comprehensions → Generate summaries.
#
# 📝 Example Interaction
# Welcome to Student Grade Management System!
#
# 1. Add Student
# 2. View All Students
# 3. Calculate Class Average
# 4. Search Student
# 5. Update Grades
# 6. Remove Student
# 7. Generate Report
# 8. Exit
#
# Enter your choice: 1
#
# Enter student name: Alice
# Enter student age: 17
# Enter grades (comma-separated): 85, 90, 78
#
# Student added successfully!
