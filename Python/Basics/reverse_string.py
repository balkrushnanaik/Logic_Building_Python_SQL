# 47. Write a Python program to reverse a string.
from os.path import join

name = 'Balkrushna'


#  Method 1
reverse_name = list(name)
reverse_name.reverse()
word = ''.join(reverse_name)
print(word)

# print(reverse_name)
# for item in reverse_name:
#     print(item,end='')


# Method 2
print('\n')
print(name[::-1])

# Method 3

