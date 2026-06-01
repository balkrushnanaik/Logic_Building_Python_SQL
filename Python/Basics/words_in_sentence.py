# 49. Write a Python program to count words in a sentence.

# method 1

intro = 'My name is Balkrushna'
count_words = intro.split()
print(f'Number of words :{len(count_words)}')

# method 2

# intro = 'My name is Balkrushna'
count = 1
for ch in intro:
    if ch == ' ':
        count += 1
print(f'Number of words in Introduction: {count}')
