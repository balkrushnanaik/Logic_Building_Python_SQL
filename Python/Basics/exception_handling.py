# Exception Handling in Python: 

# Exception handling is a mechanism in Python that allows you to handle and manage errors or exceptions that may occur during the execution of a program.
# It provides a way to gracefully handle errors and prevent the program from crashing.
# The try, except, else, and finally blocks are used for exception handling in Python.

number = input("Enter a number: ")
try:
    result = 10 / int(number)
except ValueError:
    print("Invalid input! Please enter a valid integer.")
except ZeroDivisionError:
    print("Error! Division by zero is not allowed.")
except Exception as e:
    print(f"An unexpected error occurred: {e}")
else:
    print(f"Result: {result}")
finally:
    print("Execution completed.")
    print("This block will always execute, regardless of whether an exception occurred or not.")