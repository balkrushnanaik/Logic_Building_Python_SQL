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
sentence = sentence.replace(" ", "_")
print(f"Sentence with spaces replaced by underscores: {sentence}")
# Remove all vowels from a string.
vowels = "aeiouAEIOU"
sentence = sentence.replace(vowels, "")
print(f"Sentence with vowels removed: {sentence}")
# Find the index of the first occurrence of a character.
text = "Hello, World!"
char_index = text.index("o")
print(f"Index of the first occurrence of 'o': {char_index}")
# Check whether a string starts with a given prefix.
text = "Hello, World!"
prefix = "Hello"
if text.startswith(prefix):
    print(f"The string starts with '{prefix}'.")
else:
    print(f"The string does not start with '{prefix}'.")
# Check whether a string ends with a given suffix.
text1 = "balkrushna naik"
suffix = "balkrushna"
if text1.endswith(suffix):
    print(f"The string ends with '{suffix}'.")
else:
    print(f"The string does not end with '{suffix}'.")

# Count uppercase letters, lowercase letters, digits, and special characters.
email = "balkrushnanaik9322@gmail.com"
uppercase_count = sum(1 for c in email if c.isupper())
lowercase_count = sum(1 for c in email if c.islower())
digit_count = sum(1 for c in email if c.isdigit())
special_count = sum(1 for c in email if not c.isalnum())

print(f"Uppercase letters: {uppercase_count}")
print(f"Lowercase letters: {lowercase_count}")
print(f"Digits: {digit_count}")
print(f"Special characters: {special_count}")

# 🟡 Intermediate String Questions (21–40)
# Find the frequency of every character in a string.
char_freq = {}
for char in email:
    char_freq[char] = char_freq.get(char, 0) + 1
print("Character frequencies:")
for char, freq in char_freq.items():
    print(f"'{char}': {freq}")

# Find the first non-repeating character.
first_non_repeating = None
for char in email:
    if char_freq[char] == 1:
        first_non_repeating = char
        break
print(f"First non-repeating character: {first_non_repeating}")

# Find the first repeating character.
first_repeating = None
for char in email:
    if char_freq[char] > 1:
        first_repeating = char
        break
print(f"First repeating character: {first_repeating}")
# Remove duplicate characters while maintaining order.
unique_chars = []
for char in email:
    if char not in unique_chars:
        unique_chars.append(char)
print(f"String with duplicate characters removed: {''.join(unique_chars)}")
# Check whether two strings are anagrams.
str1 = input("String 1: ")
str2 = input("String 2: ")
if sorted(str1) == sorted(str2):
    print("The strings are anagrams.")
else:
    print("The strings are not anagrams.")
# Find the longest word in a sentence.
sentence = "This is a sample sentence."
words = sentence.split()
longest_word = max(words, key=len)
print(f"Longest word: {longest_word}")
# Find the shortest word in a sentence.
shortest_word = min(words, key=len)
print(f"Shortest word: {shortest_word}")
# Reverse every word in a sentence.
# Example:
# Input: "I love Python"
# Output: "I evol nohtyP"
sentence = "I love Python"
reversed_words_sentence = " ".join(word[::-1] for word in sentence.split())
print(f"Sentence with each word reversed: {reversed_words_sentence}")

# Reverse the order of words.
# Example:
# Input: "I love Python"
# Output: "Python love I"
# Count the frequency of each word in a sentence.
sentence = "This is a sample sentence. This is another sample sentence."
word_freq = {}
for word in sentence.split():
    word_freq[word] = word_freq.get(word, 0) + 1
print("Word frequencies:")
for word, freq in word_freq.items():
    print(f"'{word}': {freq}")
# Remove all duplicate words from a sentence.
unique_words = list(dict.fromkeys(sentence.split()))
print(f"Sentence with duplicate words removed: {' '.join(unique_words)}")
# Find the most frequent character.
string = "This is a sample string."
char_freq = {}  
for char in string:
    char_freq[char] = char_freq.get(char, 0) + 1    
print("Character frequencies:")
for char, freq in char_freq.items():
    print(f"'{char}': {freq}")

# Find the second most frequent character.
sorted_chars = sorted(char_freq.items(), key=lambda x: x[1], reverse=True)
if len(sorted_chars) >= 2:
    print(f"Second most frequent character: '{sorted_chars[1][0]}' with frequency {sorted_chars[1][1]}")
else:
    print("Not enough unique characters.")

# Check whether one string is a rotation of another.
# Example:
# "ABCD" and "CDAB" → True

# Find the longest substring without repeating characters.
s = "abcabcbb"
start = 0
max_length = 0
char_index_map = {}

for end in range(len(s)):
    if s[end] in char_index_map:
        start = max(start, char_index_map[s[end]] + 1)
    char_index_map[s[end]] = end
    max_length = max(max_length, end - start + 1)

print(f"Length of the longest substring without repeating characters: {max_length}")

# Compress a string.
# Example:
# Input: "aaabbcccc"
# Output: "a3b2c4"
# Expand a compressed string.
# Example:
# Input: "a3b2c4"
# Output: "aaabbcccc"
# Find all duplicate characters and their counts.
sentence = "This is a sample sentence."
char_freq = {}
for char in sentence:
    char_freq[char] = char_freq.get(char, 0) + 1
print("Duplicate characters and their counts:")
for char, freq in char_freq.items():
    if freq > 1:
        print(f"'{char}': {freq}")
    else:
        print(f"'{char}': {freq} (not a duplicate)")
# Check whether two strings are exactly one edit away (insert, delete, or replace one character).
string1 = "pale"
string2 = "ple"
if len(string1) == len(string2):
    # Check for replacement
    found_difference = False
    for c1, c2 in zip(string1, string2):
        if c1 != c2:
            if found_difference:
                print("Strings are not one edit away.")
                break
            found_difference = True
    else:
        print("Strings are one edit away (replacement).")
# Find the longest palindromic substring.
s1 = "babad"

def expand_around_center(s, left, right):
    while left >= 0 and right < len(s) and s[left] == s[right]:
        left -= 1
        right += 1
    return right - left - 1

def longest_palindrome(s):
    if len(s) == 0:
        return ""
    
    start, end = 0, 0
    
    for i in range(len(s)):
        len1 = expand_around_center(s, i, i)      # Odd length palindrome
        len2 = expand_around_center(s, i, i + 1)  # Even length palindrome
        max_len = max(len1, len2)
        
        if max_len > (end - start):
            start = i - (max_len - 1) // 2
            end = i + max_len // 2
            
    return s[start:end + 1]