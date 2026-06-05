# 38. Write a Python program to count the digits in a number.


num = int(input("Enter a number: "))

count = 0

if num == 0:
    count = 1
else:
    num = abs(num)  # Handles negative numbers
    while num > 0:
        num //= 10
        count += 1

print("Number of digits:", count)