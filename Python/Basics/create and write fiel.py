# 86. Write a Python program to create and write into a file.

# text = open('file.txt','w')
#
# text.write('Hello My Name is Balkrushna')
# text.close()
#
# print('File create and write successfully')

file = open('file.txt','r')
content = file.read()
print(content)