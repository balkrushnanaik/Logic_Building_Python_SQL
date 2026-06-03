# 75. Write a Python program to handle file not found exception.

try:
    file = open('sample.txt', 'r')
    content = file.read()
    file.close()
except FileNotFoundError:
    print('File Not found ')