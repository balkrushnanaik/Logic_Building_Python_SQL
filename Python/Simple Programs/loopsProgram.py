# ### 3. Loops (41–60)

# 41. Print numbers from 1 to 10.
for i in range(1, 11):
    print(i)
# 42. Print numbers from 10 to 1.
for i in range(10, 0, -1):
    print(i)
# 43. Print even numbers from 1 to 100.
for i in range(2, 101, 2):
    print(i)
# 44. Print odd numbers from 1 to 100.
for i in range(1, 101, 2):
    print(i)
# 45. Find sum of first N numbers.
N = int(input("Enter the value of N: "))
sum = 0
for i in range(1, N + 1):
    sum += i
print(f"The sum of first {N} numbers is {sum}.")
# 46. Find factorial of a number.
# 47. Generate multiplication table.
num = int(input("Enter a number: "))
for i in range(1, 11):
    print(f"{num} x {i} = {num * i}")

# 48. Reverse a number.
# num = int(input("Enter a number: "))
# 49. Count digits in a number.
num = int(input("Enter a number: "))
count = 0
while num > 0:
    num //= 10
    count += 1
print(f"The number of digits is {count}.")

# 50. Find sum of digits.
num1 = int(input("Enter a number: "))
sum_of_digits = 0
while num1 > 0:
    sum_of_digits += num1 % 10
    num1 //= 10
print(f"The sum of digits is {sum_of_digits}.")

# 51. Find product of digits.
num2 = int(input("Enter a number: "))
product_of_digits = 1
while num2 > 0:
    product_of_digits *= num2 % 10
    num2 //= 10
print(f"The product of digits is {product_of_digits}.")

# 52. Check Armstrong number.

# 53. Print Fibonacci series.
# 54. Check prime number.
# 55. Print prime numbers between 1 and 100.
# 56. Find GCD of two numbers.
# 57. Find LCM of two numbers.
# 58. Print star pattern.
# 59. Print number pattern.
# 60. Print pyramid pattern.