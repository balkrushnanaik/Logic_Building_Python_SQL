# 69. Write a Python program to count even and odd numbers in a list.
count_even = 0
count_odd = 0
list1 = [1,2,3,4,1,2,3,4,6,4,3,1,2,4,5,5,6,7,7,8,9,4,6,8,8]

for i in list1:
     # print(i)
     if i % 2 == 0:
         count_even += 1
     else:
         count_odd += 1

print(f'Total Even numbers: {count_even}')
print(f'Total odd numbers: {count_odd}')


