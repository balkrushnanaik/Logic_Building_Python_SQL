# 57. Write a Python program to create a function to find factorial of a number.

import math

# def factorial():
#     print(math.factorial(5))
# factorial()


def factorial(n,fact):
    for i in range(1,n+1):
        fact = fact * i
    print(f'The factorial of {n} is : {fact}')

factorial(5,1)


