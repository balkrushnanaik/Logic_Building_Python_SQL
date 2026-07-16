# Functions in Python : 

# Functions are reusable blocks of code that perform a specific task. They help in organizing code, improving readability, and reducing redundancy.
# Functions are defined using the 'def' keyword, followed by the function name and parentheses.
# Functions can take parameters (inputs) and return values (outputs). Parameters allow you to pass data into the function, while return values allow the function to send data back to the caller.
# Functions can be called multiple times with different arguments, making them versatile and efficient.
# Functions can also have default parameter values, allowing you to call the function without providing all arguments.  


def multiply(a, b):
    """This function takes two numbers as input and returns their product."""
    return a * b

# Example usage of the multiply function
result = multiply(5, 3)
print("The product of 5 and 3 is:", result)

# Functions can also be defined with default parameter values, allowing you to call the function without providing all arguments.   

def greet(name, greeting="Hello"):
    """This function takes a name and an optional greeting message, and prints a greeting."""
    print(f"{greeting}, {name}!")
greet("Alice")  # Using the default greeting
greet("Bob", "Hi")  # Providing a custom greeting

# Functions can also return multiple values as a tuple, allowing you to return more than one piece of information from a single function call.
def get_name_and_age():
    name = "Alice"
    age = 30
    return name, age

# Example usage of the get_name_and_age function
person_name, person_age = get_name_and_age()
print(f"{person_name} is {person_age} years old.")

# Functions can also be defined with variable-length arguments, allowing you to pass a varying number of arguments to the function. This is done using the *args and **kwargs syntax.
def sum_numbers(*args):
    """This function takes a variable number of arguments and returns their sum."""
    return sum(args)    

# Example usage of the sum_numbers function
total = sum_numbers(1, 2, 3, 4, 5)
print("The sum of the numbers is:", total)