# Week 4: Control Structures
#
# Control structures allow a program to make decisions and repeat actions. In Python, we use if-else statements for
# decision-making and loops to repeat tasks.
#

# In simple terms, a control structure in programming is like giving a set of instructions with conditions on how and
# when they should be followed.
#
# Think of it like this:
#
# If you('re cooking and the recipe says, "If the water is boiling, add the pasta," that’s a decision-making (if-else) '
#        'control structure.)
# If you('re brushing your teeth and you move your brush in circles again and again until your teeth are clean, '
#        'that’s a loop (repetition) control structure.)
# If you are following a step-by-step guide to assemble furniture, that’s a sequential control structure.
# In short, control structures help a program decide what to do next based on conditions or repeating patterns.

# 1️⃣ If-Else Statements: Conditional Logic
#
# 🔹 What is an If-Else Statement?
#
# An if-else statement is used to make decisions in Python. It checks a condition:
#
# If the condition is True, it runs a block of code.
#
# If the condition is False, it runs a different block (the else part).
#
# 🎯 Real-Life Example:
#
# Imagine you are checking the weather to decide whether to take an umbrella:
#
# If it's raining, you take an umbrella.
#
# Otherwise, you go without one.
#
# 📝 Python Example:

weather = "rainy"
if weather == "rainy":
    print("Take an umbrella!")
else:
    print("No umbrella needed.")


# Take an umbrella!

#  Nested If-Else (Multiple Conditions)
#
# Sometimes, we need to check multiple conditions using elif (else if).

score = 75
if score >= 90:
    print("Grade: A")
elif score >= 80:
    print("Grade: B")
elif score >= 70:
    print("Grade: C")
else:
    print("Grade: F")

# OUTPUT: Grade: C
# ✅ Key Takeaways:
#
# ✔️ if checks a condition.✔️ elif adds more conditions.✔️ else runs when all conditions fail.

# 2️⃣ For Loops: Iterating Over Sequences
#
# 🔹 What is a For Loop?
#
# A for loop is used to repeat a task for a fixed number of times. It is mostly used to go through (iterate) a list,
# tuple, string, or range of numbers.
#
# 🎯 Real-Life Example:
#
# Imagine you have a list of names and you want to call out each person one by one.
#
# 📝 Python Example:

names = ["Alice", "Bob", "Charlie"]
for name in names:
    print("Hello,", name)

# OUTPUT
# Hello, Alice
# Hello, Bob
# Hello, Charlie

for i in range(5):
    print("Iteration:", i)

# OUTPUT
#
# Iteration: 0
# Iteration: 1
# Iteration: 2
# Iteration: 3
# Iteration: 4

# Loop Control Statements
#
# break: Stop the loop completely.
#
# continue: Skip the current iteration and move to the next one.

for number in range(5):
    if number == 3:
        break  # Stops the loop when number is 3
    print(number)


# OUTPUT
# 0
# 1
# 2

# ✅ Key Takeaways:
#
# ✔️ for loops are used for repeating tasks.✔️ range(n) repeats n times.✔️ break stops the loop early.
# ✔️ continue skips an iteration.

# 3️⃣ While Loops: Conditional Looping
#
# 🔹 What is a While Loop?
#
# A while loop keeps running as long as a condition is True.
#
# 🎯 Real-Life Example:
#
# Imagine you are filling a bucket with water:
#
# You keep adding water while the bucket is not full.
#
# Once full, you stop.
#
# 📝 Python Example:

water_level = 0
while water_level < 5:
    print("Adding water...")
    water_level += 1

# OUTPUT
# Adding water...
# Adding water...
# Adding water...
# Adding water...
# Adding water...

#  Using break in While Loops
#
# We can use break to stop the loop when a condition is met.
x = 1
while x < 10:
    if x == 5:
        break  # Stops when x is 5
    print(x)
    x += 1

# Output:
# 1
# 2
# 3
# 4

# 🔹 Using continue in While Loops
#
# We can use continue to skip an iteration and move to the next.

x = 0
while x < 5:
    x += 1
    if x == 3:
        continue  # Skips when x is 3
    print(x)

# Output:
# 1
# 2
# 4
# 5

# ✅ Key Takeaways:
#
# ✔️ while loops run as long as a condition is True.✔️ Be careful to avoid infinite loops (always update the condition)
# ✔️ break stops the loop.✔️ continue skips the current iteration.

# 4️⃣ List Comprehension
#
# 🔹 What is List Comprehension?
#
# List comprehension provides a short way to create lists.

numbers = [x+3 for x in range(5)]
print(numbers)

# Output:
# [0, 1, 2, 3, 4]

# ✅ Key Takeaway:
#
# ✔️ It is a concise way to create lists using a loop in one line.


# 5️⃣ Dictionary Comprehension
#
# 🔹 What is Dictionary Comprehension?
#
# Dictionary comprehension provides a short way to create dictionaries.
#
# 📝 Python Example:

squares = {x: x*x for x in range(5)}
print(squares)

# Output
# {0: 0, 1: 1, 2: 4, 3: 9, 4: 16}

# ✅ Key Takeaway:
#
# ✔️ It is a concise way to create dictionaries using a loop in one line.

# +------------------------+--------------------------------------+-------------------------------------------+
# | Control Structure      | Purpose                              | Example                                   |
# +------------------------+--------------------------------------+-------------------------------------------+
# | if-else               | Makes a decision                     | if age > 18: print("Adult") else: print("Minor") |
# | for loop             | Repeats a task a fixed number of times | for i in range(5): print(i)              |
# | while loop           | Repeats a task while a condition is True | while x < 5: print(x)                   |
# | break               | Stops a loop early                     | if x == 3: break                         |
# | continue            | Skips an iteration                     | if x == 3: continue                      |
# | List Comprehension  | Creates lists concisely                | [x for x in range(5)]                    |
# | Dictionary Comprehension | Creates dictionaries concisely     | {x: x*x for x in range(5)}               |
# +------------------------+--------------------------------------+-------------------------------------------+


# Assignment: If-Else Statements
# 🔹 Task: Write a Python program that asks the user for their age and determines the following:
#
# If the user is below 13, print "You are a child."
# If the user is between 13 and 19, print "You are a teenager."
# If the user is 20 or older, print "You are an adult."

# Assignment: For Loops
# 🔹 Task: Write a Python program that takes a number n from the user and prints the first n multiples of 3.
#
# 🔹 Example Input & Output:


# Assignment: While Loops
# 🔹 Task: Create a simple guessing game where:
#
# The program randomly chooses a number between 1-10.
# The user must keep guessing until they find the correct number.
# If the guess is incorrect, the program should say "Try again!".
# If the guess is correct, print "Congratulations! You guessed it right." and exit the loop.
# 🔹 Hint: Use the random module to generate a random number.


# Assignment: Break Statement
# 🔹 Task: Write a program that asks the user to enter numbers continuously.
#
# If the user enters -1, the program should stop immediately using break.
# Otherwise, it should print "Number added: <number>".

# Assignment: Continue Statement
# 🔹 Task: Write a Python program that prints all numbers from 1 to 10, except 5 and 7.
#
# Use continue to skip these numbers.


# Assignment: List Comprehension
# 🔹 Task: Given a list of numbers [1, 2, 3, 4, 5, 6, 7, 8, 9, 10], create a new list containing only the even
# numbers using list comprehension.
#
# 🔹 Expected Output:

# Assignment: Dictionary Comprehension
# 🔹 Task: Given a list of numbers [1, 2, 3, 4, 5], create a dictionary where:
#
# The keys are the numbers from the list.
# The values are the squares of the numbers.
# 🔹 Expected Output:

