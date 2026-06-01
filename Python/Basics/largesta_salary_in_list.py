import heapq
# Method 1
salary = [2,5,8,9,3,56,78,23,45,67]
# salary.sort(reverse=True)
# print(salary)
# print(salary[:5])

# 5 largest Salary from List
# Method 2
print(heapq.nlargest(5,salary))
print(heapq.nsmallest(5,salary))

