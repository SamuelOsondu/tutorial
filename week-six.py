# Week 6: Object-Oriented Programming (OOP)
# Introduction
# Imagine you're designing a car factory. Every car shares common features like wheels, an engine, and seats, but each
# car model can have different designs, colors, and functionalities.
#
# Instead of manually building each car from scratch, you define a blueprint (a class) that describes a car’s general
# structure. From this blueprint, you can create many cars (objects) with specific attributes.
#
# This is exactly how Object-Oriented Programming (OOP) works in Python! OOP allows you to create reusable blueprints
# (classes) that can be used to create multiple instances (objects).
#
# 1️⃣ Classes and Objects
# 🔹 What is a Class?
# A class is a blueprint for creating objects. It defines the attributes (variables) and methods (functions)
# that describe the object.
#
# 🔹 What is an Object?
# An object is an instance of a class. You can create multiple objects from the same class, just like producing multiple
# cars from a blueprint.
#
# 📚 Defining a Class and Creating an Object

# 1️⃣ Functions: Perform Actions
# A function is a reusable block of code that performs a specific task and optionally returns a value.
#
# Example of a Function:
def add_numbers(a, b):
    return a + b

result = add_numbers(3, 5)
print(result)  # Output: 8

# ✅ Functions focus on actions—they take input, process it, and return a result.
#
# 2️⃣ Classes: Create Objects with Attributes & Methods
# A class is a blueprint for creating objects that have both data (attributes) and behavior (methods).

# Example of a Class:

class Calculator:
    def ___init___(self):  # Constructor
        self.history = []  # Attribute (data)

    def add(self, a, b):  # Method (behavior)
        result = a + b
        self.history.append(result)  # Storing result in history
        return result

# Creating an object
calc = Calculator()

# Using the object
print(calc.add(3, 5))  # Output: 8
print(calc.history)  # Output: [8]

# ✅ Classes group data and actions together—they define a structure (blueprint) that can be used to create
# multiple objects.
#
# 3️⃣ Key Differences Between Functions and Classes
# Feature	Function	Class
# Purpose	Performs a specific task	Defines a blueprint for creating objects
# Data Storage	Doesn't store data (unless using global variables)	Stores data inside objects (attributes)
# Reusability	Reusable, but independent	Can be used to create multiple objects with similar behavior
# State Management	Stateless (does not maintain memory of previous calls)	Stateful (stores values inside attributes)

# Example
def greet():
    print("Hello!")

class Person:
    def greet(self):
        print("Hello!")

# 4️⃣ When to Use a Function vs. a Class?
# 👉 Use a function when:
# ✅ You only need to perform a specific calculation or action (e.g., add_numbers(3,5)).
# ✅ There is no need to store any state or attributes (e.g., one-time operations like sorting a list).
#
# 👉 Use a class when:
# ✅ You need to store and manage data (e.g., self.history in Calculator).
# ✅ You need to create multiple instances that share common attributes and behaviors (e.g., multiple Car objects).
# ✅ You need inheritance or polymorphism (i.e., extending functionality from a parent class).
#
# 5️⃣ Example: Function vs. Class Comparison
# Function Version (Simple, Stateless)

def add(a, b):
    return a + b

print(add(3, 5))  # Output: 8
# 👉 Just performs the addition, does not store anything.
#
# Class Version (Stateful, Structured)


class Calculator:
    def ___init___(self):
        self.history = []  # Stores past calculations

    def add(self, a, b):
        result = a + b
        self.history.append(result)  # Storing result
        return result


# Creating an object
calc = Calculator()
print(calc.add(3, 5))  # Output: 8
print(calc.history)  # Output: [8]

# 👉 Stores data and provides structure for multiple calculations.
#
# Conclusion:
# ✔️ Functions are good for one-time tasks where you don’t need to store data.
# ✔️ Classes are better for managing data and behavior together in reusable objects.


# Defining a Class

class Car:
    def ___init___(self, make, model):
        self.make = make
        self.model = model

# Creating an Object (Instance)
my_car = Car("Toyota", "Red")

# Accessing Attributes
print(my_car.brand)  # Output: Toyota
print(my_car.color)  # Output: Red

#
# ✅ Key Takeaways:
# ✔️ A class defines the blueprint for an object.
# ✔️ An object is an instance of a class.
# ✔️ The ___init___ method is the constructor that initializes an object’s attributes.

# 2️⃣ Methods: Defining and Using Instance Methods
# 🔹 What is a Method?
# A method is a function inside a class that performs an action related to the object.
#
# 📚 Defining Methods in a Class

class Car:
    def ___init___(self, brand, color):
        self.brand = brand
        self.color = color

    def start(self):
        print(f"{self.brand} is starting...")

    def move(self):
        print(f"{self.brand} is moving...")


# Creating an Object
my_car = Car("Toyota", "Red")

# Calling a Method
my_car.start()  # Output: Toyota is starting...
my_car.move()

# ✅ Key Takeaways:
# ✔️ Methods are functions inside a class.
# ✔️ The first parameter in a method is always self, which represents the current instance of the object.





# 3️⃣ Inheritance: Parent and Child Classes
# 🔹 What is Inheritance?
# Inheritance allows a new class to inherit attributes and methods from an existing class (parent class).
# This helps with code reusability.
#
# 📚 Creating a Parent and Child Class
# Parent Class
class Vehicle:
    def ___init___(self, brand):
        self.brand = brand

    def start(self):
        print(f"{self.brand} is starting...")


# Child Class (inherits from Vehicle)
class Car(Vehicle):
    def ___init___(self, brand, color):
        super().___init___(brand)  # Call parent constructor
        self.color = color

# Creating an Object of the Child Class
my_car = Car("Toyota", "Red")
my_car.start()  # Output: Toyota is starting...

# ✅ Key Takeaways:
# ✔️ Inheritance allows a child class to use methods and attributes from a parent class.
# ✔️ super().___init___() is used to call the constructor of the parent class.
#

# 4️⃣ Polymorphism and Encapsulation
# 🔹 Polymorphism: Same Method, Different Behavior
# Polymorphism allows different classes to have methods with the same name but different implementations.

class Dog:
    def speak(self):
        return "Woof!"

class Cat:
    def speak(self):
        return "Meow!"

# Using Polymorphism
animals = [Dog(), Cat()]

for animal in animals:
    print(animal.speak())

# Output:
# Woof!
# Meow!


# ✅ Key Takeaways:
# ✔️ Polymorphism allows different classes to have methods with the same name but different behaviors.
#
# 🔹 Encapsulation: Hiding Data
# Encapsulation means restricting direct access to an object's data and modifying it only through methods.

class BankAccount:
    def ___init___(self, balance):
        self.__balance = balance  # Private variable

    def deposit(self, amount):
        self.__balance += amount
        return self.__balance

    def withdraw(self, amount):
        if amount <= self.__balance:
            self.__balance -= amount
        else:
            print("Insufficient funds")
        return self.__balance

# Creating an Object
account = BankAccount(1000)

# Accessing private variable (this will give an error)
# print(account.__balance)  # AttributeError

# Using Methods to Access Private Data
print(account.deposit(500))  # Output: 1500
print(account.withdraw(300))  # Output: 1200

# ✅ Key Takeaways:
# ✔️ Encapsulation restricts direct access to certain attributes by making them private (__attribute).
# ✔️ We interact with private data only through methods.



# Problem Scenario
# A logistics company manages a fleet of vehicles. Different types of vehicles (cars, trucks, and motorcycles) exist, and each type has a different way of delivering goods.
#
# All vehicles can start and stop (common behavior).
# Cars deliver small packages
# Trucks deliver heavy goods
# Motorcycles deliver urgent courier items
# Instead of writing separate classes for each vehicle from scratch, we use inheritance to define a Vehicle parent class and specialized child classes (Car, Truck, Motorcycle).
#


# Solution: Using Inheritance & Polymorphism
# We define a Vehicle base class and let different vehicle types inherit from it while overriding the deliver_goods() method for polymorphic behavior.

# Parent class
class Vehicle:
    def ___init___(self, brand):
        self.brand = brand

    def start(self):
        print(f"{self.brand} is starting...")

    def stop(self):
        print(f"{self.brand} is stopping...")

    def deliver_goods(self):
        """This method will be overridden by child classes"""
        pass

# Child class: Car
class Car(Vehicle):
    def ___init___(self, brand, color):
        super().___init___(brand)
        self.color = color

    def deliver_goods(self):
        print(f"{self.brand} Car is delivering small packages.")

# Child class: Truck
class Truck(Vehicle):
    def ___init___(self, brand, capacity):
        super().___init___(brand)
        self.capacity = capacity  # Truck has extra attribute: capacity in tons

    def deliver_goods(self):
        print(f"{self.brand} Truck is delivering {self.capacity} tons of goods.")

# Child class: Motorcycle
class Motorcycle(Vehicle):
    def ___init___(self, brand, speed):
        super().___init___(brand)
        self.speed = speed  # Motorcycle has an extra attribute

    def deliver_goods(self):
        print(f"{self.brand} Motorcycle is delivering urgent courier items at {self.speed} km/h.")

# Using polymorphism: Function that calls `deliver_goods()`
def dispatch_vehicle(vehicle):
    vehicle.start()
    vehicle.deliver_goods()
    vehicle.stop()

# Creating different vehicle objects
car = Car("Toyota", "Red")
truck = Truck("Volvo", 10)
motorcycle = Motorcycle("Yamaha", 80)

# Dispatching different vehicles (Polymorphism in action)
dispatch_vehicle(car)
dispatch_vehicle(truck)
dispatch_vehicle(motorcycle)


# Why is this a Perfect Example?
# ✅ Inheritance: Car, Truck, and Motorcycle inherit common behaviors (start() and stop()) from Vehicle.
# ✅ Polymorphism: The dispatch_vehicle() function works with any vehicle type because they all have a deliver_goods() method.
# ✅ Scalability: If a new vehicle type (e.g., a Drone) is added, it only needs to override deliver_goods(), and everything else will still work!
# ✅ Code Reusability: No need to repeat start() and stop() logic for each vehicle type.


# Perfect Use Case for Encapsulation
# Let's consider a Bank Account System, where encapsulation ensures that sensitive data like the account balance is not directly accessed or modified from outside the class.

# Problem Scenario
# A banking system needs to protect user account details, ensuring:
#
# Balance cannot be directly accessed or modified from outside.
# Deposits and withdrawals are done through secure methods with validation.


# Solution: Using Encapsulation
# We use private attributes (__balance) and define getter and setter methods to access and modify the balance securely.


class BankAccount:
    def ___init___(self, account_holder, initial_balance=0):
        self.account_holder = account_holder
        self.__balance = initial_balance  # Private attribute (Encapsulation)

    # Getter method to check balance
    def get_balance(self):
        return self.__balance

    # Setter method to deposit money securely
    def deposit(self, amount):
        if amount > 0:
            self.__balance += amount
            print(f"Deposited {amount}. New balance: {self.__balance}")
        else:
            print("Deposit amount must be positive.")

    # Setter method to withdraw money securely
    def withdraw(self, amount):
        if 0 < amount <= self.__balance:
            self.__balance -= amount
            print(f"Withdrawn {amount}. New balance: {self.__balance}")
        else:
            print("Insufficient balance or invalid amount.")

# Creating a bank account
my_account = BankAccount("John Doe", 500)

# Accessing balance securely using getter
print(f"Current balance: {my_account.get_balance()}")  # ✅ Allowed

# Trying to deposit and withdraw securely
my_account.deposit(200)  # ✅ Allowed
my_account.withdraw(100)  # ✅ Allowed

# Trying to modify balance directly (Encapsulation prevents this)
# my_account.__balance = 100000  ❌ This will NOT work

# Direct access will fail, but we can still check balance through the method
print(f"Final balance: {my_account.get_balance()}")


# Why is this a Perfect Example?
# ✅ Encapsulation: __balance is private and cannot be accessed directly.
# ✅ Secure Access: The only way to modify balance is through deposit() and withdraw(), preventing accidental changes.
# ✅ Data Integrity: Prevents invalid operations like negative deposits or over-withdrawals.


# 🔥 Summary
# Concept	Purpose	Example
# Classes & Objects	Create blueprints and instances	class Car: pass
# Methods	Define actions for objects	def start(self): pass
# Inheritance	Allow child classes to inherit from parents	class Car(Vehicle): pass
# Polymorphism	Same method, different behavior	def speak(self): pass
# Encapsulation	Hiding data using private attributes	self.__balance = balance

# 📝 Practice Questions
# Classes & Objects:
#
# Create a Student class with attributes name, age, and grade.
# Create a method get_grade() that returns the student's grade.


# Methods:
#
# Modify the Student class to include a method is_passing() that returns True if the grade is above 50.


# Inheritance:
#
# Create a Teacher class that inherits from Person and has a subject attribute.


# Polymorphism:
#
# Create two classes Circle and Square, both having a method area(). Implement area() differently for both.
# Encapsulation:


# Create a BankAccount class with a private balance attribute and methods deposit() and withdraw(). Ensure withdraw()
# checks if there are sufficient funds.


# 🎯 CLASSWORK
# 📌 Mini Project: Library Management System
# Create a Library System using OOP with the following features:
#
# Book Class
#
# Attributes: title, author, year
# Method: display_info()
# Library Class
#
# Stores a collection of books
# Methods: add_book(), remove_book(), show_books()
# Borrower Class
#
# Attributes: name, borrowed_books
# Methods: borrow_book(), return_book()
# ✅ Implement these classes and simulate borrowing and returning books in Python!
