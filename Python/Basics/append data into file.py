# 88. Write a Python program to append data into a file.

text = open('prompt.md','a')
text.write('\n Thank you for append in me in this file')
text.close()


file = open('prompt.md','r')
content = file.read()
print(content)
file.close()