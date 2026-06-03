# 71. Write a Python program to handle division by zero exception.

n = int(input('Enter a Number: '))

try:
    res = n / 0
except Exception as e:
    print(f'Exception: {e}')
else:
    print(f'Result is: {res}')
finally:
    print('Execution Completed')