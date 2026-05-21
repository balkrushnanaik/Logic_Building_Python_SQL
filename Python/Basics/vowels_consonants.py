# 22. Write a Python program to check whether a character is a vowel or consonant.
ch = input("Enter any characters: ")
vowels = 'aeiouAEIOU'

if ch in vowels:
    print('It is vowels')
else:
    print('It is consonants')