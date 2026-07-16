# Sets in Python : 

# Sets are a built-in data type in Python that represent an unordered collection of unique elements. 
# They are useful for performing mathematical set operations such as union, intersection, and difference.
# Sets are defined using curly braces {} or the set() constructor.
# If you try to add duplicate elements to a set, they will be automatically ignored, ensuring that all elements remain unique.
# Sets are mutable, meaning you can add or remove elements after the set has been created.
# sets does not support indexing, slicing, or other sequence-like behavior, as they are unordered collections.  
# sets are commonly used for membership testing, removing duplicates from a list, and performing set operations.
# sets methods include add(), remove(), discard(), pop(), clear(), union(), intersection(), difference(), and symmetric_difference().


data1 = {1, 2, 3, 4, 5}  #
data2 = {4, 5, 6, 7, 8}

# Union of two sets
# Union of two sets combines all unique elements from both sets, eliminating duplicates.
union_set = data1.union(data2)
print("Union of data1 and data2:", union_set)

# Intersection of two sets
# Intersection of two sets returns a new set containing only the elements that are present in both sets.
intersection_set = data1.intersection(data2)    
print("Intersection of data1 and data2:", intersection_set)

# Difference of two sets
# Difference of two sets returns a new set containing elements that are present in the first set but not in the second set.
difference_set = data1.difference(data2)
print("Difference of data1 and data2:", difference_set)

# Symmetric Difference of two sets
# Symmetric difference of two sets returns a new set containing elements that are present in either of the sets but not in both.
symmetric_difference_set = data1.symmetric_difference(data2)
print("Symmetric Difference of data1 and data2:", symmetric_difference_set)

# Adding and Removing Elements from a Set
# You can add elements to a set using the add() method and remove elements using the remove() or discard() methods. 
# The remove() method raises a KeyError if the element is not found, while discard() does not raise an error.

data1.add(6)  # Adding an element to the set
print("After adding 6 to data1:", data1)

data1.remove(2)  # Removing an element from the set
print("After removing 2 from data1:", data1)    

data1.discard(10)  # Discarding an element that may not exist in the set
print("After discarding 10 from data1:", data1)  # No error is raised, and the set remains unchanged
