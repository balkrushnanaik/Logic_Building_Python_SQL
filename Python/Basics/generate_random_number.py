# 82. Write a Python program to generate random numbers.
import random
while True:
    numbers = random.randint(1, 100)
    print(numbers)

    if numbers > 90:
        break


