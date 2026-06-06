# 34. Write a Python program to find the sum of first N natural numbers.

n = 10
count = 0

for i in range(1,n+1):
    # print(i,end=' ')
    count += i
print(count)

# Method 2

n = 10
sum_n = n * (n + 1) // 2
print(sum_n)

