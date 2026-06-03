# 73. Write a Python program demonstrating finally block.

n1 = int(input('Enter a number:'))
n2 = int(input('Enter a number: '))

try:
    res = n1 / n2
except Exception as e:
    print(f'Exception is: {e}')
else:
    print(f'Result is: {res}')
finally:
    print('Done')
