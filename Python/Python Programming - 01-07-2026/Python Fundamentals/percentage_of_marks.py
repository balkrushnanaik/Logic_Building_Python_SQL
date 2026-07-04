# 52. Write a program to calculate the percentage of five subject marks.

def percentage(math,sci,phy,chem,bio):
    total = math + sci + phy + chem + bio
    per = total / 5
    return per

stud1 = percentage(99,88,78,89,74)
print(f'Student1: {stud1:.2f}%')
