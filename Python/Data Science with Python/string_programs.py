# 🟢 Basic String Questions (1–20)
# Print a string.
print("Hello, World!")
# Take a string as input and display it.
user_input = input("Enter a string: ")
print(user_input)
# Find the length of a string.
text = "Hello, World!"
print(len(text))
# Convert a string to uppercase.
name = "python"
print(name.upper())
# Convert a string to lowercase.
print(name.lower())
# Count the occurrence of a given character.
name = "banana"
print(name.count("n"))
# Check whether a character exists in a string.
for n in name:
    if n == "a":
        print("Character 'a' exists in the string.")
        break
# Reverse a string.
text = "Hello, World!"
print(text[::-1])
# Print the first and last character.
print(text[0])
print(text[-1])
# Remove leading and trailing spaces.
text = "  Hello, World!  "
print(text.strip())
# Count the number of vowels.
vowels = "aeiouAEIOU"
count = 0
for char in text:
    if char in vowels:
        count += 1
# Count the number of consonants.
count_consonants = 0
for char in text:
    if char.isalpha() and char not in vowels:
        count_consonants += 1
# Check whether a string is a palindrome.
text = input("Enter a string to check for palindrome: ")
if text == text[::-1]:
    print("The string is a palindrome.")
else:
    print("The string is not a palindrome.")
# Count the number of words in a sentence.
sentence = "This is a sample sentence."
word_count = len(sentence.split())
print(f"Number of words in the sentence: {word_count}")
# Replace all spaces with underscores (_).
# Remove all vowels from a string.
# Find the index of the first occurrence of a character.
# Check whether a string starts with a given prefix.
# Check whether a string ends with a given suffix.
# Count uppercase letters, lowercase letters, digits, and special characters.

# 🟡 Intermediate String Questions (21–40)
# Find the frequency of every character in a string.
# Find the first non-repeating character.
# Find the first repeating character.
# Remove duplicate characters while maintaining order.
# Check whether two strings are anagrams.
# Find the longest word in a sentence.
# Find the shortest word in a sentence.
# Reverse every word in a sentence.
# Example:
# Input: "I love Python"
# Output: "I evol nohtyP"
# Reverse the order of words.
# Example:
# Input: "I love Python"
# Output: "Python love I"
# Count the frequency of each word in a sentence.
# Remove all duplicate words from a sentence.
# Find the most frequent character.
# Find the second most frequent character.
# Check whether one string is a rotation of another.
# Example:
# "ABCD" and "CDAB" → True
# Find the longest substring without repeating characters.
# Compress a string.
# Example:
# Input: "aaabbcccc"
# Output: "a3b2c4"
# Expand a compressed string.
# Example:
# Input: "a3b2c4"
# Output: "aaabbcccc"
# Find all duplicate characters and their counts.
# Check whether two strings are exactly one edit away (insert, delete, or replace one character).
# Find the longest palindromic substring.