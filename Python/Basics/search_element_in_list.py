# 67. Write a Python program to search an element in a list.


names = ['Rahul','Sukhdev','Pranjal','Vaibhav','Sara','Prachi']


search = input('Enter name : ').capitalize()

if search in names:
    print(f'{search} name is in the list')
else:
    print(f'{search} name is not in the list')