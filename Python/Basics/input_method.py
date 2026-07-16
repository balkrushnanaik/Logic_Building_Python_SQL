# Input Method in Python: 

# The input() function in Python is used to take user input from the console. It reads a line of text entered by the user and returns it as a string.
# The input() function can also take an optional prompt string as an argument, which is displayed to the user before they enter their input. This helps guide the user on what kind of input is expected.
# The input() function always returns the input as a string, so if you need to work with other data types (like integers or floats), you will need to convert the input using functions like int() or float().  
# Example usage of the input() function:

name = input("Enter your name: ")  # Prompting the user to enter their name
age = int(input("Enter your age: "))  # Prompting the user to enter their age

print(f"Hello, {name}! You are {age} years old.")  # Displaying the user's name and age

# The input() function can also be used to take multiple inputs from the user in a single line. You can use the split() method to separate the inputs based on a delimiter (like space) and store them in a list or tuple.
values = input("Enter multiple values separated by space: ").split()
print("The values entered are:", values)    