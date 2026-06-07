# 78. Write a Python program to find GCD of two numbers.

num1 = 48
num2 = 18

while num2 != 0:
    num1, num2 = num2, num1 % num2

print("GCD =", num1)