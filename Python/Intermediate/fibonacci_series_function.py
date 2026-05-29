'''
Fibonacci Series:
0 1 1 2 3 5 8 13
'''

print(__doc__)

def fibonacci(a,b,n):
    for i in range(n):
        print(a, end=' ') # 0
        next_sum = a + b # 1
        a = b
        b = next_sum


fibonacci(0,1,8)