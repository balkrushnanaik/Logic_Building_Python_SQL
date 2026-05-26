# Pattern
'''
A
A B
A B C
A B C D
A B C D E
A B C D E F
A B C D E F G
'''

n = int(input('Enter n: '))

for i in range(1,n+1):
    for j in range(65, 65 + i):
        print(chr(j), end=' ')

    print()

# ASCII - American Standard Code For Information Interchange
'''
A 65
B 66
c 67
d 68 
so on

chr is used to do 65 = A, 66 = B ..........
'''
