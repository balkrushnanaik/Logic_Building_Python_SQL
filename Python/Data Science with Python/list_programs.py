# 🟢 List (15 Problems)

# 1. Create a list of 10 numbers and print it.
num = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
for i in num:
    print(f"{i}", end=" ")
# 2. Find the length of a list.
num1 = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
length = len(num1)
print(f"\nLength of the list is: {length}")
# 3. Print the first and last element of a list.
num2 = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
first_element = num2[0]
last_element = num2[-1]
print(f"First element: {first_element}")
print(f"Last element: {last_element}")
# 4. Add an element at the end of a list.
num3 = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
# num3.append(11)
num3.extend([11,12,13,14])  # Using extend we can add multiple element at the end of list
print(f"List after adding an element at the end: {num3}")

# 5. Insert an element at a specific position.
num4 = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
num4.insert(5, 99)  # Insert 99 at index 5
print(f"List after inserting an element at index 5: {num4}")
# 6. Remove a given element from a list.
num5 = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
num5.remove(5)  # Remove the element 5 from the list
print(f"List after removing the element 5: {num5}")
# 7. Find the largest number in a list.
num6 = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
largest = max(num6)
print(f"The largest number in the list is: {largest}")
# 8. Find the smallest number in a list.
num7 = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
smallest = min(num7)    
print(f"The smallest number in the list is: {smallest}")
# 9. Calculate the sum of all elements in a list.
# 10. Count how many times a given number appears.
# 11. Reverse a list without using slicing.
# 12. Sort a list in ascending and descending order.
# 13. Remove duplicate elements from a list.
# 14. Merge two lists into one.
# 15. Find the second largest number in a list.