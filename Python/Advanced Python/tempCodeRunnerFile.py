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
        print(f"Percentage:{self.marks[0]+self.marks[1]+self.marks[2] / 3 * 100}")


student1 = Student("Balkrushna", [80, 75, 90])
student1.calculate_percentage()