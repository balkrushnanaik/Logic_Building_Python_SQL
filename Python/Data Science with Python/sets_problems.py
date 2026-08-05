# # 🔵 Set (10 Problems)

# 26. Create a set of integers.
set1 = {1, 2, 3, 4, 5}
# 27. Add a new element to a set.
set1.add(6)
print(f"Set after adding an element: {set1}")
# 28. Remove an element from a set.
set1.remove(3)
print(f"Set after removing an element: {set1}")
# 29. Find the union of two sets.
set2 = {4, 5, 6, 7, 8}
union_set = set1.union(set2)
print(f"Union of set1 and set2: {union_set}")
# 30. Find the intersection of two sets.
intersection_set = set1.intersection(set2)
print(f"Intersection of set1 and set2: {intersection_set}")
# 31. Find the difference between two sets.
difference_set = set1.difference(set2)
print(f"Difference of set1 and set2: {difference_set}")
# 32. Check whether an element exists in a set.
element_exists = 6 in set1
print(f"Element 6 exists in set1: {element_exists}")
# 33. Remove duplicate values from a list using a set.
list_with_duplicates = [1, 2, 2, 3, 4, 4, 5]
unique_list = list(set(list_with_duplicates))
print(f"List with unique values: {unique_list}")
# 34. Find elements present in one set but not in another.
# 35. Check whether two sets are disjoint.