# 72. Write a Python program to handle invalid user input using try-except.

try:
    num = int(input("Enter an integer: "))
    print("You entered:", num)

except ValueError:
    print("Invalid input! Please enter a valid integer.")


