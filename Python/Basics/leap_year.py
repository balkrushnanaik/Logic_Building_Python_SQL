year = int(input('Enter a year: '))

if year % 100 == 0 and year % 400 == 0:
    print(f'Year {year} is a leap year')
elif year % 4 == 0 and year % 100 != 0:
    print(f'Year {year} is a leap year')
else:
    print(f'Year {year} is not leap year')

print('Thank you!')
