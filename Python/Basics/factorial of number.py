# 35. Write a Python program to calculate the factorial of a number.

n = 5
fact = 1

for i in range(1,n+1):
    fact *= i
print(fact)

# Method 2

import math

n = 5
print(math.factorial(n))