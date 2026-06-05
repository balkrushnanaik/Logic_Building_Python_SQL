# Find the sum of digits of a number

num = int(input("Enter a number: "))

sum_digits = 0

num = abs(num)  # Handles negative numbers

while num > 0:
    digit = num % 10
    sum_digits += digit
    num = num // 10

print("Sum of digits:", sum_digits)