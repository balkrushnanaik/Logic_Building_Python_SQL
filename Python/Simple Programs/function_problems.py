# ### 7. Functions (93–96)

# 93. Create a function to add two numbers.
def add_numbers(a, b):
    return a + b
add = add_numbers(5, 10)
print(f"The sum of 5 and 10 is {add}.")
# 94. Create a function to check prime number.

# 95. Create a function to calculate factorial.
def factorial(n,fact):
    for i in range(1,n+1):
        fact = fact * i
    print(f'The factorial of {n} is : {fact}')
factorial(5,1)
# 96. Create a recursive Fibonacci function.