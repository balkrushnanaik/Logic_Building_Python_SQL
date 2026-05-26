# Fibonacci series
# 0 1 1 2 3 5 8 13

n = 8
a = 0
b = 1
print('Fibonacci Series: ')
for i in range(n):
    print(a,end=' ') # a = 0
    next_num = a + b # next_num = 1
    a = b
    b = next_num

