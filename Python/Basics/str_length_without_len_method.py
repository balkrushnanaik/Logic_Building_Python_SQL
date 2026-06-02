# 52. Write a Python program to find the length of a string without using len().

# method 1
# name = 'Balkrushna'
# count = 0
# list1 = list((name))
# print(list1)
#
# for ch in list1:
#     if ch in list1:
#         count += 1
# print(f"Length of String: {count}")

# method 2
name = 'Balkrushna'

count = 0

for ch in name:
    count += 1

print(f"Length of String: {count}")




