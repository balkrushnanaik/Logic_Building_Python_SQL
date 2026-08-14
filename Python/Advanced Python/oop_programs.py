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
class Book:
    def __init__(self, title, author, price):
        self.title = title
        self.author = author
        self.price = price

    def display(self):
        print(f"Book Name   : {self.title}")
        print(f"Author Name : {self.author}")
        print(f"Price       : {self.price}")
        print()


book1 = Book("IKIGAI", "XYZ", 200)
book2 = Book("Soumya", "Balkrushna", 100000)
book3 = Book("Python Basics", "ABC", 500)

book1.display()
book2.display()
book3.display()

# Student Marks
# Create a Student class with name and marks for three subjects. Create a method calculate_percentage() that returns the student's percentage.
class Student:
    def __init__(self, name, marks):
        self.name = name
        self.marks = {
            "Hindi": marks[0],
            "Marathi": marks[1],
            "English": marks[2]
        }

    def calculate_percentage(self):
        print(f"Name: {self.name}")

        total = (
            self.marks["Hindi"] +
            self.marks["Marathi"] +
            self.marks["English"]
        )

        percentage = total / 300 * 100

        print(f"Percentage: {percentage:.2f}%")


student1 = Student("Balkrushna", [80, 75, 90])
student1.calculate_percentage()
   
# Employee Salary
# Create an Employee class with name and salary. Create a method calculate_bonus() that gives a 10% bonus on the salary.
class Employee:
    def __init__(self, name, salary):
        self.name = name
        self.salary = salary

    def calculate_bonus(self):
        bonus = self.salary * 0.10
        print(f"Name: {self.name}")
        print(f"Salary: ${self.salary}")
        print(f"Bonus: ${bonus}")

employee1 = Employee("Alice", 50000)
employee1.calculate_bonus()

# Product Discount
# Create a Product class with name and price. Create a method apply_discount(discount) that calculates the final price after discount.
class Product:
    def __init__(self, name, price):
        self.name = name
        self.price = price

    def apply_discount(self, discount):
        final_price = self.price - (self.price * discount / 100)
        print(f"Product: {self.name}")
        print(f"Original Price: ${self.price}")
        print(f"Final Price after {discount}% discount: ${final_price}")

product1 = Product("Laptop", 1000)
product1.apply_discount(10)

# Temperature Converter
# Create a Temperature class with temperature in Celsius. Create methods to convert Celsius to Fahrenheit and Fahrenheit to Celsius.
class Temperature:
    def __init__(self, celsius):
        self.celsius = celsius

    def to_fahrenheit(self):
        fahrenheit = (self.celsius * 9/5) + 32
        print(f"{self.celsius}°C is {fahrenheit}°F")

    def to_celsius(self, fahrenheit):
        celsius = (fahrenheit - 32) * 5/9
        print(f"{fahrenheit}°F is {celsius}°C")
temp1 = Temperature(25)
temp1.to_fahrenheit()
temp1.to_celsius(77)

# Calculator Class
# Create a Calculator class with methods:
# add()
# subtract()
# multiply()
# divide()

class Calculator:
    def add(self, a, b):
        return a + b

    def subtract(self, a, b):
        return a - b

    def multiply(self, a, b):
        return a * b

    def divide(self, a, b):
        if b != 0:
            return a / b
        else:
            return "Cannot divide by zero"
c1 = Calculator()
print(c1.add(10, 5))
print(c1.subtract(10, 5))
print(c1.multiply(10, 5))
print(c1.divide(10, 5))

# 🟠 Level 3: Basic OOP Concepts
# Inheritance – Animal
# Create a parent class Animal with a method sound(). Create child classes Dog and Cat that override the sound() method.
# Parent class
class Animal:
    def sound(self):
        print("Animal makes a sound")


# Child class
class Dog(Animal):
    def sound(self):
        print("Dog says: Woof Woof")


# Child class
class Cat(Animal):
    def sound(self):
        print("Cat says: Meow")


# Creating objects
dog = Dog()
cat = Cat()

dog.sound()
cat.sound()

# Inheritance – Vehicle
# Create a parent class Vehicle with attributes brand and speed. Create a child class Bike with an additional attribute gear.
# Parent class
class Vehicle:
    def __init__(self, brand, speed):
        self.brand = brand
        self.speed = speed


# Child class
class Bike(Vehicle):
    def __init__(self, brand, speed, gear):
        super().__init__(brand, speed)
        self.gear = gear


# Create Bike object
bike = Bike("Honda", 120, 5)

print("Brand:", bike.brand)
print("Speed:", bike.speed, "km/h")
print("Gear:", bike.gear)
# Encapsulation – Bank Account
# Create a BankAccount class with a private variable __balance. Create methods deposit(), withdraw(), and get_balance() to access the balance safely.
class BankAccount:
    def __init__(self, balance):
        self.__balance = balance

    def deposit(self, amount):
        self.__balance += amount
        print("Amount deposited:", amount)

    def withdraw(self, amount):
        if amount <= self.__balance:
            self.__balance -= amount
            print("Amount withdrawn:", amount)
        else:
            print("Insufficient balance")

    def get_balance(self):
        return self.__balance


# Create object
account = BankAccount(5000)

account.deposit(2000)
account.withdraw(1000)

print("Current Balance:", account.get_balance())
# Polymorphism – Shapes
# Create classes Circle, Rectangle, and Triangle. Each class should have an area() method. Create objects and call area() using the same method name.
import math

# Circle class
class Circle:
    def __init__(self, radius):
        self.radius = radius

    def area(self):
        return math.pi * self.radius ** 2


# Rectangle class
class Rectangle:
    def __init__(self, length, width):
        self.length = length
        self.width = width

    def area(self):
        return self.length * self.width


# Triangle class
class Triangle:
    def __init__(self, base, height):
        self.base = base
        self.height = height

    def area(self):
        return 0.5 * self.base * self.height


# Create objects
circle = Circle(5)
rectangle = Rectangle(10, 5)
triangle = Triangle(8, 6)

# Same method name used for different objects
print("Circle Area:", circle.area())
print("Rectangle Area:", rectangle.area())
print("Triangle Area:", triangle.area())
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