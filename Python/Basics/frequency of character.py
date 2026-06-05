# Count frequency of characters in a string

text = input("Enter a string: ")

freq = {}

for char in text:
    if char in freq:
        freq[char] += 1
    else:
        freq[char] = 1

print("Character Frequencies:")
for char, count in freq.items():
    print(char, ":", count)