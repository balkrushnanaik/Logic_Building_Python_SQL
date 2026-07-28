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
num3 = int(input("Enter a number: "))
order = len(str(num3))
sum_of_powers = sum(int(digit) ** order for digit in str(num3))
if sum_of_powers == num3:   
    print(f"{num3} is an Armstrong number.")
else:
    print(f"{num3} is not an Armstrong number.")        

# 53. Print Fibonacci series.
n = int(input("Enter the number of terms: "))
a, b = 0, 1
for _ in range(n):
    print(a, end=' ')
    a, b = b, a + b

# 54. Check prime number.
num4 = int(input("Enter a number: "))
if num4 > 1:
    for i in range(2, int(num4 ** 0.5) + 1):
        if num4 % i == 0:
            print(f"{num4} is not a prime number.")
            break
    else:
        print(f"{num4} is a prime number.")
# 55. Print prime numbers between 1 and 100.
# 56. Find GCD of two numbers.
# 57. Find LCM of two numbers.
# 58. Print star pattern.
n = int(input("Enter the number of rows: "))
for i in range(1, n + 1):
    print('*' * i)
    
# 59. Print number pattern.
num = int(input("Enter the number of rows: "))
for i in range(1, num + 1):
    for j in range(1, i + 1):
        print(j, end=' ')
    print()

# 60. Print pyramid pattern.
num = int(input("Enter the number of rows: "))
for i in range(1, num + 1):
    print(' ' * (num - i) + '*' * (2 * i - 1))
