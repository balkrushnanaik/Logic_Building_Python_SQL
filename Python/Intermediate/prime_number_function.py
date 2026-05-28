# 58. Write a Python program to create a function to check prime numbers.
from idlelib.debugobj_r import remote_object_tree_item


def prime(num):

    if num <= 1:
        print('Not prime nor composite')
        return
    for i in range(2,num):
        if num % i == 0:
            print('Not Prime')
            return
    print('Prime')
prime(2)

