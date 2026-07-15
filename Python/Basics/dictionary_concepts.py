# Dictionary concepts in Python: 

# - Dictionaries keys are unique and immutable, while values can be of any data type and can be duplicated.
# - Dictionaries are unordered collections of key-value pairs, where each key is associated with a value

# - Dictionaries are defined using curly braces {} and key-value pairs are separated by colons (:).
# Dictionaries can be created using the dict() constructor or by using curly braces {}.

# - Dictionaries can be accessed using keys, and values can be modified or updated by assigning a new value to an existing key.
# - Dictionaries can be iterated using loops, and they support various built-in functions and methods for operations like adding, removing, or checking for the existence of keys.

# Dictionaries are commonly used for tasks such as data storage, configuration settings, and mapping relationships between different pieces of data.

Students = {
    "Name": ["Balkrushna", "Alice", "Eve", "Charlie", "David", "Frank", "Grace", "Heidi", "Ivan", "Judy", "Mallory", "Niaj", "Olivia", "Peggy", "Sybil", "Trent", "Victor", "Walter"],
    "Age": [20, 21, 22, 23, 24, 25, 26, 27, 28, 29, 30, 31, 32, 33, 34, 35, 36, 37],
    "Gender": ["Male", "Female", "Female", "Male", "Male", "Male", "Female", "Female", "Male", "Female", "Female", "Male", "Female", "Female", "Female", "Male", "Male", "Male"],
    "Marks": [85, 90, 78, 92, 88, 95, 80, 75, 89, 91, 87, 93, 82, 84, 86, 94, 81, 83],
    "Grade": ["A", "A", "B", "A", "B", "A", "B", "C", "B", "A", "B", "A", "C", "B", "B", "A", "C", "B"]
}

print("Students Dictionary:", Students)

for key, value in Students.items():
    print(f"{key}: {value}")

print(f"Length of Students Dictionary: {len(Students)}")
print(f"Keys in Students Dictionary: {list(Students.keys())}")

print(Students["Name"][0], Students["Age"][0], Students["Gender"][0], Students["Marks"][0], Students["Grade"][0])  # Accessing value using key
