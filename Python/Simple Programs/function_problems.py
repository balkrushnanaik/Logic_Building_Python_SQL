# ### 7. Functions (93–96)

# 93. Create a function to add two numbers.
def add_numbers(a, b):
    return a + b
add = add_numbers(5, 10)
print(f"The sum of 5 and 10 is {add}.")
# 94. Create a function to check prime number.
num = 29
def is_prime(n):
    if n <= 1:
        return False
    for i in range(2, int(n**0.5) + 1):
        if n % i == 0:
            return False
    return True
print(f"{num} is prime: {is_prime(num)}")

# 95. Create a function to calculate factorial.
def factorial(n,fact):
    for i in range(1,n+1):
        fact = fact * i
    print(f'The factorial of {n} is : {fact}')
factorial(5,1)
# 96. Create a recursive Fibonacci function.