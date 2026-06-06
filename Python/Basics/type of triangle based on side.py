# 30. Write a Python program to determine the type of triangle based on sides.

side1 = 2
side2 = 2
side3 = 2

if side1 == side2 == side3:
    print('Equilateral Triangle')
elif side1 == side2 or side2 == side3 or side1 == side3:
    print('Isosceles Triangle')
else:
    print('Scalene Triangle')
