# 70. Write a Python program to merge two lists.

list1 = [12,1,3,4,1,2,4,5]
list2 = list([1,2,34,5,67])

# 1.
# merge = list1 + list2
# print(merge)

# 2.
# list1.extend(list2)
# print(list1)

# 3.
for i in list2:
    list1.append(i)
print(list1)
