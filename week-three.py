# WEEK 3 ---> Data Structures
# What is a "data structure"?

# What is "Data"??

# Data is simply information, probably in digital form. It can be numbers, words, images, videos, or anything that conveys meaning.

# Examples of Data in Real Life:
# Your name is data.
# Your phone number is data.
# A list of students' scores in a test is data.
# A photo on your phone is also data.
# Computers use data to store, process, and analyze information. When we use Python, we work with data all the time—whether it’s numbers, text, or more complex information.

# What then is "data structure"?
# A data structure is a way of organizing and storing data so that it can be used efficiently.
#
# Think of it like this:
#
# A bookshelf is a data structure for storing books.
# A shopping list is a data structure for keeping track of items you want to buy.
# A contacts list on your phone is a data structure that stores names and phone numbers.
# In Python, there are different types of data structures, including:
#
# Lists – like a shopping list 📋
# Tuples – like a list but cannot be changed 📌
# Dictionaries – like a phonebook with key-value pairs 📖

# +----------------+----------------------+----------------------------------+
# | Data Structure | Type                 | Use Case                         |
# +----------------+----------------------+----------------------------------+
# | list           | Ordered, Mutable      | General storage, iteration       |
# | tuple          | Ordered, Immutable    | Fixed collections                |
# | dict           | Key-Value Mapping     | Quick lookups                    |
# | set            | Unordered, Unique     | Removing duplicates, fast lookups|
# | frozenset      | Immutable Set         | Read-only collections            |
# | deque          | Fast Queue            | Fast operations from both ends   |
# | OrderedDict    | Ordered Dictionary    | Keeps insertion order            |
# | defaultdict    | Dictionary with Defaults | Avoids `KeyError`              |
# | namedtuple     | Tuple with Named Fields | Readable structured data       |
# | heapq          | Priority Queue        | Efficient sorting, task scheduling |
# | queue.Queue    | Thread-Safe Queue     | Multi-threading queues           |
# | str            | Immutable Sequence    | Storing and manipulating text    |
# +----------------+----------------------+----------------------------------+

# 1. Lists (Ordered Collection of Items)
# A list is like a shopping list. It holds multiple values inside square brackets [ ].

fruits = ["apple", "banana", "cherry"]
print(fruits[0])  # Output: apple

# List Methods (Useful Tools for Lists)
# Method	What It Does	Example
# append(item)	Adds an item to the end	fruits.append("mango")
# remove(item)	Removes an item	fruits.remove("banana")
# sort()	Sorts the list	fruits.sort() Has to be of same datatype.
# reverse()	Reverses the order	fruits.reverse()

numbers = [5, 2, 9, 1]
numbers.sort()
print(numbers)  # Output: [1, 2, 5, 9]

# # List Comprehensions (Shorter Way to Create Lists)  ---> Should be studied after we treat for loop.
# squares = [x**2 for x in range(5)]
# print(squares)  # Output: [0, 1, 4, 9, 16]

# Lists in Python 📝
# A list is a collection of items stored in a specific order.
#
# ✅ Example of a List:

fruits = ["apple", "banana", "cherry", "date", "elderberry"]

# 1. Indexing in Lists 🔢
# Indexing is how we access items in a list using their position (index number).
#
# Python uses Zero-Based Indexing:
# Item	apple	banana	cherry	date	elderberry
# Index	0	1	2	3	4
# Negative Index	-5	-4	-3	-2	-1

# fruits = ["apple", "banana", "cherry", "date", "elderberry"]
#
# print(fruits[0])  # Output: apple
# print(fruits[2])  # Output: cherry
# print(fruits[-1]) # Output: elderberry (last item)
# print(fruits[-3]) # Output: cherry


# 2. Slicing in Lists ✂️
# Slicing allows you to extract a portion of a list using this syntax:

# list[start:stop:step]

fruits = ["apple", "banana", "cherry", "date", "elderberry"]

print(fruits[1:4])  # Output: ['banana', 'cherry', 'date']
print(fruits[:3])   # Output: ['apple', 'banana', 'cherry'] (from start to index 2)
print(fruits[2:])   # Output: ['cherry', 'date', 'elderberry'] (from index 2 to end)
print(fruits[-3:-1]) # Output: ['cherry', 'date'] (negative indices work too!)
print(fruits[::2])  # Output: ['apple', 'cherry', 'elderberry'] (step = 2, skip one each time)
print(fruits[::-1]) # Output: ['elderberry', 'date', 'cherry', 'banana', 'apple'] (reversed list)

# 3. List Methods 🛠️
# Python provides many built-in methods for lists.
#
# Method	Description	Example
# append(x)	Adds x to the end of the list	fruits.append("fig")
# insert(i, x)	Inserts x at index i	fruits.insert(1, "grape")
# remove(x)	Removes the first occurrence of x	fruits.remove("banana")
# pop(i)	Removes and returns item at i	fruits.pop(2)
# index(x)	Returns the index of x	fruits.index("cherry")
# count(x)	Counts occurrences of x	fruits.count("apple")
# sort()	Sorts the list in ascending order	fruits.sort()
# reverse()	Reverses the list order	fruits.reverse()
# extend(list2)	Adds items from list2	fruits.extend(["fig", "grape"])
# clear()	Removes all elements	fruits.clear()

# ✅ Example Using Some Methods:
# fruits = ["apple", "banana", "cherry"]
# fruits.append("date")
# print(fruits)  # Output: ['apple', 'banana', 'cherry', 'date']
#
# fruits.insert(1, "grape")
# print(fruits)  # Output: ['apple', 'grape', 'banana', 'cherry', 'date']
#
# fruits.pop(2)
# print(fruits)  # Output: ['apple', 'grape', 'cherry', 'date']
#
# fruits.sort()
# print(fruits)  # Output: ['apple', 'cherry', 'date', 'grape']


# Lists Practice Questions
# Create a list of 5 fruits and print the third fruit.
# Add "Mango" to the list using .append().
# Remove "Banana" from the list using .remove().
# Sort the list in reverse alphabetical order.
# Create a new list with the squares of numbers from 1 to 5 using list comprehension.

# Assignment
# 1. Lists Assignment 📝
# Objective: Practice list indexing, slicing, and built-in methods.
#
# Task 1: Create and Access a List
# Create a list of 5 different colors.
# Print the first and last color using indexing.
# Print a slice containing the second and third colors.
# Task 2: Modify a List
# Create a list of 5 numbers.
# Add a new number to the list using append().
# Insert a number at the second position using insert().
# Remove the third number from the list using remove().
# Use pop() to remove the last item and print the removed item.
# Task 3: Sorting and Reversing
# Create a list of 6 random numbers.
# Sort the list in ascending order using sort().
# Reverse the list using reverse().

# _____________________TUPLES____________________________
# 2. Tuples (Lists That Cannot Change)

# A tuple is similar to a list, but the key difference is that tuples are immutable, meaning you cannot change, add, or remove elements after creation.
# A tuple is like a locked list—you can't add or remove items.
# ✅ Example of a Tuple:
fruits = ("apple", "banana", "cherry", "date")

# Indexing in Tuples 🔢

colors = ("red", "blue", "green")
print(colors[1])  # Output: blue


# 1.3 Why Use Tuples? 🤔
# Feature	Explanation
# Immutable	Cannot be changed after creation (more secure).
# Faster	Tuples are faster than lists in Python.
# Safe for Data	Best when data should not be modified.


# 1.4 Tuple Methods 🛠️
# Method	Description	Example
# count(x)	Counts occurrences of x	fruits.count("apple")
# index(x)	Returns index of x	fruits.index("cherry")

fruits = ("apple", "banana", "cherry", "banana")

print(fruits.count("banana"))  # Output: 2
print(fruits.index("cherry"))  # Output: 2


# 1.5 Tuple Packing & Unpacking 📦
# ✅ Tuple Packing (Grouping Multiple Values):

person = ("John", 30, "Engineer")
print(person)  # Output: ('John', 30, 'Engineer')

# ✅ Tuple Unpacking (Extracting Values):
name, age, job = person
print(name)  # Output: John
print(age)   # Output: 30
print(job)   # Output: Engineer

# Tuples Practice Questions
# What is the difference between a list and a tuple?
# Create a tuple with 4 colors and print the second one.
# Try adding a new color to the tuple. What happens?
# Convert the tuple to a list, add a new color, then convert it back to a tuple.
# Use tuple unpacking to assign ("John", 25, "Engineer") to three variables.

# 2. Tuples Assignment 📝
# Objective: Understand how to use tuples, and practice with indexing and built-in methods.
#
# Task 1: Create and Access a Tuple
# Create a tuple of 5 different animals.
# Print the first and last animal using indexing.
# Print the last animal using negative indexing.
# Task 2: Tuple Methods
# Create a tuple with repeated numbers: (1, 2, 3, 2, 4, 2, 5).
# Use the count() method to count how many times 2 appears.
# Use the index() method to find the position of 4.
# Try modifying an item in the tuple. What happens? Write your observation.


# _______________________DICTIONARIES_______________________
# 3. Dictionaries (Key-Value Pairs, Like a Phonebook)
# A dictionary is like a real dictionary—each word (key) has a meaning (value).
student = {
    "name": "John",
    "age": 25,
    "course": "Computer Science"
}

# 2.1 Accessing Dictionary Values 🔑
# ✅ Using Keys to Get Values:

print(student["name"])  # Output: John
print(student["age"])   # Output: 25

# Using .get() (Prevents Errors):
print(student.get("course"))  # Output: Computer Science
print(student.get("height", "Not Found"))  # Output: Not Found

# 2.2 Dictionary Methods 🛠️
# Method	Description	Example
# keys()	Returns all keys	student.keys()
# values()	Returns all values	student.values()
# items()	Returns key-value pairs	student.items()
# update()	Updates dictionary	student.update({"age": 26})
# pop(x)	Removes key x and returns value	student.pop("course")
# clear()	Removes all items	student.clear()

# Method	What It Does	Example
# keys()	Shows all keys	person.keys()
# values()	Shows all values	person.values()
# items()	Shows key-value pairs	person.items()

student = {"name": "John", "age": 25, "course": "Computer Science"}

print(student.keys())   # Output: dict_keys(['name', 'age', 'course'])
print(student.values()) # Output: dict_values(['John', 25, 'Computer Science'])

student.update({"age": 26})  # Updating a value
print(student)  # Output: {'name': 'John', 'age': 26, 'course': 'Computer Science'}

student = {"name": "John", "age": 25, "course": "Computer Science"}

print(student.keys())   # Output: dict_keys(['name', 'age', 'course'])
print(student.values()) # Output: dict_values(['John', 25, 'Computer Science'])

student.update({"age": 26})  # Updating a value
print(student)  # Output: {'name': 'John', 'age': 26, 'course': 'Computer Science'}


# Dictionaries Practice Questions
# Create a dictionary with keys: "name", "age", and "city".
# Print only the keys of the dictionary.
# Add a new key "country" with a value.
# Use .pop() to remove "city".
# Write a loop to print both keys and values in the dictionary.

#
# 3. Dictionaries Assignment 📝
# Objective: Practice creating, modifying, and retrieving dictionary values.
#
# Task 1: Create and Access a Dictionary
# Create a dictionary with three students, using their names as keys and their ages as values.
# Print the age of the second student using key-based indexing.
# Use the get() method to access a student’s age safely.
# Task 2: Modify a Dictionary
# Add a new student to the dictionary.
# Update the age of one of the students.
# Delete a student from the dictionary.
# Task 3: Dictionary Methods
# Print all the keys using the keys() method.
# Print all the values using the values() method.
# Print all the key-value pairs using the items() method.
