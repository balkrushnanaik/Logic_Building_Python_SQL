# 22. Write a Python program to check whether a character is a vowel or consonant.
ch = input("Enter any characters: ")
vowels = 'aeiouAEIOU'

# if ch in vowels:
#     print('Vowels')
# else:
#     print('Consonants')

# isalpha() is a string method that checks whether all characters in a string are alphabets (A-Z or a-z).
if len(ch) == 1 and ch.isalpha():
    if ch in vowels:
        print('Vowels')
    else:
        print('Consonants')
else:
    print('Please enter a single alphabet.')

