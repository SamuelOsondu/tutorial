# 1️⃣ Importing Modules
# A module is a Python file that contains functions, classes, and variables that can be reused.
#
# 📌 Importing Built-in Modules
# Python comes with a rich standard library. You can import modules like this:

import math

print(math.sqrt(25))  # Output: 5.0


# 📌 Importing Specific Functions


from random import randint

print(randint(1, 10))  # Generates a random number between 1 and 10

# 📌 Using Third-Party Modules
# Third-party modules are installed using pip.

# pip install requests

import requests

response = requests.get("https://api.github.com")
print(response.json())

# 2️⃣ Creating Modules and Packages
# 📌 Creating a Module
# A module is just a Python file.

# 👉 Create my_module.py:

def greet(name):
    return f"Hello, {name}!"

import my_module

print(my_module.greet("Alice"))


# 📌 Creating a Package
# A package is a folder that contains multiple modules and a special __init__.py file.
#
# Example Structure:

# my_package/
# │── __init__.py
# │── math_operations.py
# │── string_operations.py

# 👉 math_operations.py
def add(a, b):
    return a + b

# 👉 string_operations.py

def reverse(text):
    return text[::-1]


from my_package.math_operations import add

print(add(3, 4))  # Output: 7

# 3️⃣ Virtual Environments
# A virtual environment helps keep dependencies isolated for different projects.
#
# 📌 Creating a Virtual Environment

# python -m venv .venv


# 📌 Activating the Virtual Environment
#
# Windows:

# .venv\Scripts\activate

# pip install requests pandas

# deactivate

# 4️⃣ Introduction to Git (Version Control Basics)
# Git helps track changes in code and collaborate with others.
#
# 📌 Setting Up Git

# git config --global user.name "Your Name"
# git config --global user.email "your_email@example.com"

# git init

# git status

# git add .

# git commit -m "Initial commit"

# 5️⃣ Using Git: Branching, Merging, Resolving Conflicts
# 📌 Creating a New Branch

# git branch new-feature
# git checkout new-feature  # Switch to the new branch

# git checkout main
# git merge new-feature

# 📌 Resolving Merge Conflicts
# If there is a conflict, Git will show it inside the affected file. You will need to manually edit the file and
# resolve the differences.

# 6️⃣ Collaborating with Git: Remote Repositories & Pull Requests
# 📌 Connecting to GitHub

# git remote add origin https://github.com/your-username/repository.git
# git push -u origin main

# 📌 Cloning a Repository
#
# git clone https://github.com/your-username/repository.git
# 📌 Creating a Pull Request

# Push changes to GitHub.
#
# Open a Pull Request on GitHub.
#
# Wait for review and merge the request.

# 🔹 Summary of What You Learned
# ✔️ Importing built-in and third-party modules.
# ✔️ Creating reusable modules and packages.
# ✔️ Using virtual environments for dependency management.
# ✔️ Version control with Git: tracking changes, commits, branches.
# ✔️ Collaborating using GitHub (push, pull, merge, pull requests).
