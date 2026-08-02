#  🟡 Tuple (10 Problems)

# 16. Create a tuple with five elements.
tuple1 = (1, 2, 3, 4, 5)
print(f"Tuple with five elements: {tuple1}")
# 17. Print the first and last element of a tuple.
a, b, c, d, e = tuple1
print(f"First element: {a}")
print(f"Last element: {e}")
# 18. Count the occurrence of an element in a tuple.
tuple2 = (1, 2, 2, 3, 4, 5)
print(f"Element 2 occurs {tuple2.count(2)} times in the tuple.")
# 19. Find the index of a given element.
element = 3
index = tuple2.index(element)
print(f"Index of element {element}: {index}")
# 20. Convert a tuple into a list.
list_from_tuple = list(tuple1)
print(f"List converted from tuple: {list_from_tuple}")
# 21. Convert a list into a tuple.
list1 = [6, 7, 8, 9, 10]
tuple_from_list = tuple(list1)
print(f"Tuple converted from list: {tuple_from_list}")
# 22. Check whether an element exists in a tuple.
element_to_check = 4
if element_to_check in tuple1:
    print(f"Element {element_to_check} exists in the tuple.")
else:
    print(f"Element {element_to_check} does not exist in the tuple.")
# 23. Find the maximum and minimum values in a tuple.
max_value = max(tuple1)
min_value = min(tuple1)
print(f"Maximum value in the tuple: {max_value}")
print(f"Minimum value in the tuple: {min_value}")
# 24. Concatenate two tuples.
# 25. Create a tuple with mixed data types and print each element.