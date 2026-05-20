# 10. Write a Python program to convert kilometers into meters and centimeters.

km = int(input("Enter kilometer: "))
m = km * 1000
cm = km * 100000
print(f'{km}KM is = {m}M')
print(f'{km}KM is = {cm}CM')
