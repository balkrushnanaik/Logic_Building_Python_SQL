# 74. Write a Python program demonstrating multiple exceptions.

try:
    n1 = int(input('Enter a number: '))
    n2 = int(input('Enter a number: '))
    res = n1 / n2
except ZeroDivisionError:
    print('Cannot be divide by zero')
except ValueError:
    print('ValueError: invalid literal for int() with base 10')
else:
    print(res)
finally:
    print('Done Thank You!')