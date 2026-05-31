# 68. Write a Python program to remove duplicate elements from a list.

list1 = [1,2,1,2,3,4,2,3,4,2,1,4,5,6,7,7,9]
# print(type(list1))
# print(list1)
unique_elements = set(list1)
print(type(unique_elements))

print(f'List before remove duplicates: {list1}')
print(f'List after remove duplicates: {unique_elements}')