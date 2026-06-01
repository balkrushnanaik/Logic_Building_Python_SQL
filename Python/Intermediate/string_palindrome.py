# 48. Write a Python program to check whether a string is a palindrome.

# Method 1
# str1 = 'ANNA'
# # print(str1)
# reverse_str = str1[::-1]
#
# if str1 == reverse_str:
#     print('String is palindrome')
# else:
#     print('String is not palindrome')

# Method 2
# Check whether a string is a palindrome

str1 = 'ANNA'

reverse_str = str1[::-1]

if str1.lower() == reverse_str.lower():
    print("String is palindrome")
else:
    print("String is not palindrome")