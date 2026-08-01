list5 = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
list5.sort()
second_largest = list5[-2]
list5.sort(reverse=True)
second_lowest = list5[-2]
print(f"The second lowest number in the list is: {second_lowest}")
print(f"The second largest number in the list is: {second_largest}")