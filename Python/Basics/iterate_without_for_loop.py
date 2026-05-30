numbers = [1,2,3,4,5,6]

# for num in numbers:
#     print(num)
# not use for loop
# not use indexing

num = iter(numbers)
while True:
    try:
        print(next(num))
    except:
        break

