# Tuple Concepts in Python : Tuples are immutable sequences in Python that can hold a collection of items.
#  They are defined using parentheses () and can contain elements of different data types.
# Tuple are ordered, heterogeneous, and immutable. Once a tuple is created, its elements cannot be modified, added, or removed.
#  Tuples are often used to group related data together and can be used as keys in dictionaries due to their immutability.
# We can create a tuple using tuple() constructor or by using parentheses ().
# Tuples can be indexed and sliced like lists, allowing access to individual elements or subsets of the tuple.
# Tuple can be iterated using loops, and they support various built-in functions and methods for operations like counting occurrences of elements or finding the index of an element.


data = ("Balkrushna", "Alice", "Eve", 1, 2, True, False, 3.14, None)
print("Tuple:", data)
print(f"Length of tuple: {len(data)}")

for item in data:
    # print("Item:", item, "Type:", type(item))
    print(item, end=" ")



