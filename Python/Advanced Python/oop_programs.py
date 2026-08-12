# 🟢 Level 1: Very Basic
# Create a Student Class
# Create a Student class with attributes name, age, and course. Create an object and display the details.
class Student:
    def __init__(self, name, age, course):
        self.name = name
        self.age = age
        self.course = course

    def display_details(self):
        print(f"Name: {self.name}, Age: {self.age}, Course: {self.course}")
student1 = Student("Alice", 20, "Computer Science")
student1.display_details()
# Create a Car Class
# Create a Car class with attributes brand, model, and price. Create two objects and display their information.
class Car:
    def __init__(self, brand, model, price):
        self.brand = brand
        self.model = model
        self.price = price

    def display_info(self):
        print(f"Brand: {self.brand}, Model: {self.model}, Price: ${self.price}")
car1 = Car("Toyota", "Camry", 25000)
car2 = Car("Honda", "Civic", 22000)
car1.display_info()
car2.display_info()
# Employee Details
# Create an Employee class with name, id, and salary. Create an object and print all employee details.
class Employee:
    def __init__(self, name, emp_id, salary):
        self.name = name
        self.emp_id = emp_id
        self.salary = salary

    def display_details(self):
        print(f"Name: {self.name}, ID: {self.emp_id}, Salary: ${self.salary}")
emp1 = Employee("John Doe", "E123", 50000)
emp1.display_details()
# Person Introduction
# Create a Person class with name and age. Create a method introduce() that prints:
# "My name is ___ and I am ___ years old."
class Person:
    def __init__(self,name,age):
        self.name = name
        self.age = age
    def introduce(self):
        print(f'My name is{self.name} and I am {self.age} years old.')
p1 = Person("Soumya", 22)
p1.introduce()
# Rectangle Area
# Create a Rectangle class with length and width. Create a method area() to calculate and return the area.
class Rectangle:
    def __init__(self,length,width):
        self.length = length
        self.width = width
    def area(self):
        return self.length * self.width
r1 = Rectangle(10,20)
print(r1.area())

            
# Circle Area
# Create a Circle class with a radius attribute. Create a method area() to calculate the area of the circle.
class circle:
    def __init__(self,radius):
        self.radius = radius
    def area(self):
        return 3.14 * self.radius * self.radius
c1 = circle(5)
print(c1.area())
# Bank Account
# Create a BankAccount class with account_holder and balance. Create methods deposit() and withdraw().
class BankAccount:
    def __init__(self, account_holder, balance):
        self.account_holder = account_holder
        self.balance = balance

    def deposit(self, amount):
        self.balance += amount
        print(f"Deposited ${amount}. New balance: ${self.balance}")

    def withdraw(self, amount):
        if amount <= self.balance:
            self.balance -= amount
            print(f"Withdrew ${amount}. New balance: ${self.balance}")
        else:
            print("Insufficient funds.")
person1 = BankAccount("Alice", 1000)
person1.deposit(500)
person1.withdraw(200)
# Mobile Phone
# Create a Mobile class with brand, model, and price. Create a method display_details() to display the phone information.
class Mobile:
    def __init__(self, brand, model, price):
        self.brand = brand
        self.model = model
        self.price = price

    def display_details(self):
        print(f"Brand: {self.brand}, Model: {self.model}, Price: ${self.price}")
m1 = Mobile("Apple", "iPhone 13", 999)
m1.display_details()
# 🟡 Level 2: Constructors & Methods
# Book Class
# Create a Book class with title, author, and price. Use a constructor to initialize the values and create three book objects.
# Student Marks
# Create a Student class with name and marks for three subjects. Create a method calculate_percentage() that returns the student's percentage.
# Employee Salary
# Create an Employee class with name and salary. Create a method calculate_bonus() that gives a 10% bonus on the salary.
# Product Discount
# Create a Product class with name and price. Create a method apply_discount(discount) that calculates the final price after discount.
# Temperature Converter
# Create a Temperature class with temperature in Celsius. Create methods to convert Celsius to Fahrenheit and Fahrenheit to Celsius.
# Calculator Class
# Create a Calculator class with methods:
# add()
# subtract()
# multiply()
# divide()
# 🟠 Level 3: Basic OOP Concepts
# Inheritance – Animal
# Create a parent class Animal with a method sound(). Create child classes Dog and Cat that override the sound() method.
# Inheritance – Vehicle
# Create a parent class Vehicle with attributes brand and speed. Create a child class Bike with an additional attribute gear.
# Encapsulation – Bank Account
# Create a BankAccount class with a private variable __balance. Create methods deposit(), withdraw(), and get_balance() to access the balance safely.
# Polymorphism – Shapes
# Create classes Circle, Rectangle, and Triangle. Each class should have an area() method. Create objects and call area() using the same method name.
# Class Variable – College
# Create a Student class with name and roll_no as instance variables and college as a class variable. Create five students and display their details.

# Simple Library System ⭐
# Create a Book class and a Library class.

# The Book class should contain:

# title
# author
# is_available

# The Library class should have methods:

# add_book()
# display_books()
# borrow_book()
# return_book()

# Implement a simple system where a user can borrow and return books.