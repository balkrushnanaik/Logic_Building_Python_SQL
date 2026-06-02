# 54. Write a Python program to check whether two strings are anagrams.

'''
Two strings are anagrams if they contain the exact same characters in the exact same frequencies,
 but in a different order (e.g., "listen" and "silent").
'''
print(__doc__)

str1 = 'Listen'
str2 = 'silent'

if sorted(str1.lower()) == sorted(str2.lower()):
    print("Strings are anagrams")
else:
    print('Strings are not anagrams')