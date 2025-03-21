# # Week 7: File Handling in Python


# The Case of the Vanishing Records
# Imagine you are working as a finance officer at a company. Every day, employees submit expense reports for
# reimbursements. Your job is to review and process these reports.
#
# At first, you keep track of everything in your Python program, storing reports in a list:
#

expense_reports = [
    {"name": "John", "amount": 5000, "category": "Travel"},
    {"name": "Sarah", "amount": 2000, "category": "Office Supplies"}
]

# You review, approve, and reject reports easily. Everything seems fine—until one day, the program crashes.
#
# When you restart the program… all the records are gone!
#
# Why?
# Because the data was stored temporarily in memory (RAM) and disappeared when the program stopped running.
#
# The Solution: File Handling
# To permanently save records, you decide to:
#
# Write approved expenses to a file (expenses.csv) so they are not lost.
# Read from the file when the program starts, ensuring past records are available.
# Use JSON files to store data in a structured format for easy retrieval.
# Now, even if the program crashes or the computer restarts, all expense reports are safe and can be accessed anytime.


# ## 1. Reading and Writing Files
#
# ### Opening a File
#
# Python provides the `open()` function to work with files. The syntax is:


file = open("filename", "mode")


# - `filename`: Name of the file
# - `mode`: Specifies the mode in which the file is opened
#   - `'r'` – Read (default mode)
#   - `'w'` – Write (creates a new file if it doesn’t exist or overwrites an existing file)
#   - `'a'` – Append (adds data to an existing file without deleting its content)
#   - `'b'` – Binary mode (used for non-text files like images)
#   - `'t'` – Text mode (default, used for text files)
#   - `'r+'` – Read and write
#
# ### Reading a File

file = open("example.txt", "r")  # Open file in read mode
content = file.read()  # Read entire file content
print(content)
file.close()  # Always close the file after reading

# - `read(size)`: Reads `size` bytes of content (default reads entire file)
# - `readline()`: Reads a single line
# - `readlines()`: Reads all lines as a list
#
# Example:


file = open("example.txt", "r")
for line in file:
    print(line.strip())  # Removes extra newline characters
file.close()


### Writing to a File
#
# Using the `'w'` mode:


file = open("example.txt", "w")
file.write("Hello, Python!\n")
file.write("File handling is easy.\n")
file.close()


# - This overwrites the file’s content if it already exists.
#
# Appending Data:

file = open("example.txt", "a")
file.write("Appending new line.\n")
file.close()


# ### Using `with` Statement (Best Practice)
#
# Using `with open()` automatically closes the file:

with open("example.txt", "r") as file:
    content = file.read()
    print(content)  # File is automatically closed after block execution


# ## 2. Working with Different File Types
#
# ### Text Files
#
# - Text files store data in human-readable format (e.g., `.txt` files)
# - Default mode for `open()` is `'t'` (text mode)
#
# ### CSV Files (Comma-Separated Values)
#
# #### Writing to a CSV File
#

import csv

with open("data.csv", "w", newline='') as file:
    writer = csv.writer(file)
    writer.writerow(["Name", "Age", "City"])
    writer.writerow(["Alice", 25, "New York"])
    writer.writerow(["Bob", 30, "London"])

#
# #### Reading from a CSV File


with open("data.csv", "r") as file:
    reader = csv.reader(file)
    for row in reader:
        print(row)

#
# ### JSON Files (JavaScript Object Notation)
#
# #### Writing JSON Data

import json

data = {
    "name": "Alice",
    "age": 25,
    "city": "New York"
}

with open("data.json", "w") as file:
    json.dump(data, file)  # Convert dictionary to JSON and save


# #### Reading JSON Data


with open("data.json", "r") as file:
    data = json.load(file)  # Load JSON data into a dictionary
    print(data)


# ## 3. File Methods and Attributes
#
# - `file.name` – Returns the name of the file
# - `file.mode` – Returns the mode in which file was opened
# - `file.closed` – Returns `True` if file is closed
# - `file.seek(offset)` – Moves cursor to specified position
# - `file.tell()` – Returns current position of cursor
#
# Example:
#

with open("example.txt", "r") as file:
    print("File Name:", file.name)
    print("Mode:", file.mode)
    print("Closed?:", file.closed)


# ## Summary
# ✔ Python allows file operations like reading, writing, and appending.
# ✔ Use `with open()` for safe file handling.
# ✔ Work with different file formats like `.txt`, `.csv`, and `.json`.
# ✔ Utilize file attributes and methods for efficient file handling.

