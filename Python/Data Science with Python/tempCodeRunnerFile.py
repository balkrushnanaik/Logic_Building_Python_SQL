stud1 = {"name": "Alice", "age": 22}
stud2 = {"major": "Mathematics", "GPA": 3.7}

students = {**stud1, **stud2}
print(f"Merged dictionary: {students}")