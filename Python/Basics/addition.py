# num1 = 1000
# num2 = 100
#
# addition = num1 + num2
# print(f'Addition of {num1} and {num2} is : {addition}')
# print('Thank You!')

def students(a,b):
    return a + b

stud = students(20,20)
print(stud)

try:
    total = 10/0
    print(total)
except Exception as e:
    print(e)