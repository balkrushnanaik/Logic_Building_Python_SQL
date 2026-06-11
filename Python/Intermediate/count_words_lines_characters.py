# 1. Count words, lines, and characters in a text file.

file = open('sample.txt','r')
content = file.read()
# print(content)

char_count = len(content)
word_count = len(content.split())
line_count = len(content.splitlines())

file.close()

print(f'Number of characters are: {char_count}')
print(f'Number of words are: {word_count}')
print(f'Number of lines: {line_count}')




