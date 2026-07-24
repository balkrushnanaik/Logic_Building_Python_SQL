# ### 9. Exception Handling (99)

# 99. Handle division by zero using `try-except`.
num = int(input("Enter a number: "))
try:
    result = 10 / num
    print(f"The result of 10 divided by {num} is {result}.")    
except Exception as e:
    print(f"Error: {e}. Division by zero is not allowed.")
else:
    print(f"Division performed successfully: {result}.")
finally:
    print("Execution completed.")