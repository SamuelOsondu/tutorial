# Week 12: Building GUI Applications
# 1️⃣ GUI with Tkinter: Creating Windows, Widgets, Events
# Tkinter is a built-in Python library used for creating graphical user interfaces (GUIs). It is one of the most
# straightforward ways to build a GUI in Python. Let's break it down:
#
# What We Will Cover:
# Creating a basic window with Tkinter.
#
# Adding widgets like labels, buttons, and text fields.
#
# Handling events such as button clicks.
#
# 1.1: Basic Tkinter Window

import tkinter as tk

# Create the main window
root = tk.Tk()
root.title("My First Tkinter App")
root.geometry("400x300")

# Start the Tkinter event loop
root.mainloop()


# Widget	Description
# Label	Display text/images
# Button	Trigger actions
# Entry	Single-line text input
# Text	Multi-line text input
# Checkbutton	Checkboxes
# Radiobutton	Radio selection
# Listbox	Selectable list
# Scale	Slider input
# Canvas	For drawings/shapes/images
# Frame	Container for grouping widgets


# ✅ 3. Layout Managers
# There are three layout managers:
#
# pack() – Stack widgets vertically/horizontally
#
# grid() – Arrange in rows/columns (more control)
#
# place() – Absolute positioning
#
# We’ll focus mostly on grid() and pack().
#


# ✅ 5. Variable Tracking with StringVar, IntVar, etc.
# These help widgets dynamically update with variable changes.
#

# ✅ 6. Styling and Theming
# Customize font, color, size, borders
#
# Use ttk (Themed Tkinter) for more modern-looking widgets
#
#
# Explanation:
#
# root = tk.Tk(): Creates the main window object.
#
# root.title(): Sets the title of the window.
#
# root.geometry(): Specifies the window size.
#
# root.mainloop(): Starts the Tkinter event loop to keep the window open.


# 1.2: Adding Widgets
# Widgets are the building blocks of a GUI. You can add buttons, labels, text boxes, etc., to your window.
#
# Example: Adding Labels and Buttons
import tkinter as tk

def greet_user():
    name = entry.get()  # Retrieve text from the entry widget
    greeting_label.config(text=f"Hello, {name}!")  # Update the label text

# Create the main window
root = tk.Tk()
root.title("Greeting App")
root.geometry("400x300")

# Label widget
label = tk.Label(root, text="Enter your name:", font=("Arial", 14))
label.pack(pady=10)

# Entry widget
entry = tk.Entry(root, font=("Arial", 14))
entry.pack(pady=10)

# Button widget
button = tk.Button(root, text="Greet", font=("Arial", 14), command=greet_user)
button.pack(pady=10)

# Label for greeting
greeting_label = tk.Label(root, text="", font=("Arial", 14))
greeting_label.pack(pady=20)

# Start the Tkinter event loop
root.mainloop()

# Explanation:
#
# Label(), Entry(), and Button() are Tkinter widgets used to create different UI elements.
#
# command=greet_user: The button calls the greet_user function when clicked, which updates the greeting label
# based on user input.
#
# 1.3: Handling Events
# Events in Tkinter refer to user actions, like clicking a button or entering text. You can define functions
# to respond to these events.
#
# Example: Button Click Event
import tkinter as tk

def on_button_click():
    print("Button clicked!")

# Create main window
root = tk.Tk()
root.title("Button Click Event")
root.geometry("300x200")

# Create a button widget and bind event
button = tk.Button(root, text="Click Me", command=on_button_click)
button.pack(pady=20)

# Start the Tkinter event loop
root.mainloop()

# Explanation:
#
# The on_button_click() function gets triggered when the button is clicked.


# 2️⃣ Project Development and Best Practices
# When developing any software project, it's important to follow coding standards and implement best practices to
# ensure clean, maintainable, and efficient code.
#
# 2.1: Coding Style
# PEP 8: The official Python style guide that dictates how to format Python code.
#
# Indentation: Use 4 spaces per indentation level.
#
# Naming Conventions: Use descriptive variable names (e.g., first_name, calculate_area) and avoid single-letter
# variable names.
#
# Line Length: Limit all lines to a maximum of 79 characters.
#
# 2.2: Testing
# Unit Testing: Test individual parts of the application to make sure they work as expected.
#
# You can use Python’s built-in unittest library for testing.

import unittest

def add(x, y):
    return x + y

class TestMathFunctions(unittest.TestCase):
    def test_add(self):
        self.assertEqual(add(2, 3), 5)  # Test addition

if __name__ == "__main__":
    unittest.main()

# Explanation:
#
# The unittest.TestCase class helps to create test cases, and self.assertEqual() checks if the output is as expected.
#
# 2.3: Debugging
# Print Statements: Use print statements to debug values in your code during runtime.
#
# Using a Debugger: Python has a built-in debugger, pdb, which allows you to step through code and inspect variables.

import pdb

def add(x, y):
    pdb.set_trace()  # Debugger stops here
    return x + y

# 3️⃣ Using Git for Project Version Control and Collaboration
# Git is a tool that helps you manage changes to your codebase and allows for easy collaboration between multiple
# developers.
#
# 3.1: Initializing a Git Repository
# git init: Initialize a new Git repository.
#
# git status: Check the status of files (which ones have been modified, staged, etc.).
#
# git add <file>: Add files to the staging area.
#
# git commit -m "message": Commit changes to the repository.
#
# Steps to Set Up Git in Your Project
# # Initialize a new Git repository
# git init
#
# # Check the status of files
# git status
#
# # Add files to staging area
# git add .
#
# # Commit the changes
# git commit -m "Initial commit"
#
# # Set up a remote repository (e.g., on GitHub)
# git remote add origin <repository_url>
#
# # Push the changes to the remote repository
# git push -u origin master
# 3.2: Collaboration with Git
# Branching: Create branches for new features or bug fixes.
#
# Merging: Merge branches to integrate new features into the main codebase.

# # Create a new branch
# git checkout -b feature-xyz
#
# # Make changes, add files, and commit
#
# # Switch back to master
# git checkout master
#
# # Merge the new feature branch
# git merge feature-xyz


# 🛠️ Practical Example for Students:
# Task: Build a simple To-Do List App using Tkinter, where users can add and delete tasks.
#
# Features:
#
# Add tasks to the list.
#
# Delete tasks.
#
# Mark tasks as complete.
#
# Use Git to track project versions and share the code on GitHub.
