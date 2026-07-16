# Strings in Python : 

# Strings are a built-in data type in Python that represent sequences of characters.
# Strings are defined using either single quotes (' ') or double quotes (" ").  
# Strings are immutable, meaning that once a string is created, it cannot be changed.
#  Any operation that modifies a string will create a new string object.
# Strings can be concatenated using the + operator and repeated using the * operator.
# Strings can be indexed and sliced to access individual characters or substrings.  
# Strings support various methods for manipulation, such as upper(), lower(), strip(), replace(), split(), join(), and many more.
# Strings can also be formatted using f-strings, the format() method, or the % operator.
# Strings can be used in various applications, such as text processing, data parsing, and user input handling.

name = "Alice"
# Accessing individual characters using indexing
print("First character of name:", name[0])  # Output: A

# Slicing a string to get a substring
print("Substring of name (1 to 3):", name[1:4]) # Output: lic
print("Reversed string:", name[::-1]) # Output: ecilA

# Concatenating strings
greeting = "Hello, " + name + "!"
print(greeting)  # Output: Hello, Alice!

# f-strings for formatting
age = 30
print(f"{name} is {age} years old.")  # Output: Alice is 30 years old.

