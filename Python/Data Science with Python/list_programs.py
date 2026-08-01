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
num8 = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
total_sum = sum(num8)   
print(f"The sum of all elements in the list is: {total_sum}")
# 10. Count how many times a given number appears.
num9 = [1,2,2,3,4,5,2,3]
print(f"Given number repeat {num9.count(2)} times")
# 11. Reverse a list without using slicing.
num10 = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
reversed_list = []
for i in range(len(num10)-1, -1, -1):
    reversed_list.append(num10[i])
print(f"Reversed list: {reversed_list}")
# 12. Sort a list in ascending and descending order.
list1 = [5, 2, 9, 1, 5, 6]
# Ascending order
list1.sort()
print(f"List in ascending order: {list1}")
# Descending order
list1.sort(reverse=True)
print(f"List in descending order: {list1}")
# 13. Remove duplicate elements from a list.
list2 = [1, 2, 3, 4, 5, 1, 2, 3]
unique_list = list(set(list2))
print(f"List with unique elements: {unique_list}")
# 14. Merge two lists into one.
list3 = [1, 2, 3]
list4 = [4, 5, 6]
merged_list = list3 + list4
print(f"Merged list: {merged_list}")
# 15. Find the second largest number in a list.
list5 = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
list5.sort()
second_largest = list5[-2]
list5.sort(reverse=True)
second_lowest = list5[-2]
print(f"The second lowest number in the list is: {second_lowest}")
print(f"The second largest number in the list is: {second_largest}")