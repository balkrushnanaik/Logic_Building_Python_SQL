# ### 10. OOP (100)

# 100. Create a `Student` class with attributes (`name`, `age`, `marks`) and a method to display details.

class Student:
    def __init__(self, name, age, marks):
        self.name = name
        self.age = age
        self.marks = marks

    def display_details(self):
        print(f"Name: {self.name}")
        print(f"Age: {self.age}")
        print(f"Marks: {self.marks}")
student1 = Student("Alice", 20, 85)
student1.display_details()