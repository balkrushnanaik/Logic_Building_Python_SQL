# 24. Write a Python program to check whether a number is a multiple of 3 and 7.

num = 21

if num % 3 == 0 and num % 7 == 0:
    print(num, "is a multiple of 3 and 7")
else:
    print(num, "is not a multiple of 3 and 7")