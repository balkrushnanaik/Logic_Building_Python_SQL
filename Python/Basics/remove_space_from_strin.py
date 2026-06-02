# 51. Write a Python program to remove spaces from a string.

student_name = '                            Soumya    '
print(f'Name before remove space: {student_name}')
new_stud = student_name.strip() #strip() returns a new string
print(f'Name after remove space: {new_stud}')
