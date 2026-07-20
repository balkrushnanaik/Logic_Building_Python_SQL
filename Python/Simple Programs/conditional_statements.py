# ### 2. Conditional Statements (21–40)

# 21. Check if a number is even or odd.
number = 10
if number % 2 == 0:
    print("The number is even.")
else:
    print("The number is odd.")

# 22. Check if a number is positive, negative, or zero.
number = -5
if number > 0:
    print("The number is positive.")
elif number < 0:
    print("The number is negative.")
else:
    print("The number is zero.")

# 23. Find the largest of two numbers.
a = 10
b = 20
if a > b:
    print(f"The largest number is {a}.")
else:
    print(f"The largest number is {b}.")

# 24. Find the largest of three numbers.
a = 10
b = 20
c = 30
if a >= b and a >= c:
    print(f"The largest number is {a}.")
elif b >= a and b >= c:
    print(f"The largest number is {b}.")
else:
    print(f"The largest number is {c}.")

# 25. Check if a year is a leap year.
year = int(input('Enter a year: ')) 

if year % 100 == 0 and year % 400 == 0:
    print(f'Year {year} is a leap year')
elif year % 4 == 0 and year % 100 != 0:
    print(f'Year {year} is a leap year')
else:
    print(f'Year {year} is not leap year')

print('Thank you!')

# 26. Check voting eligibility.
age = 19
result = "eligible" if age >= 18 else "not eligible"
print(f"You are {result} to vote.")

# 27. Check whether a character is a vowel or consonant.
# 28. Check if a number is divisible by 5 and 11.
# 29. Check whether a character is uppercase or lowercase.
# 30. Find smallest of three numbers.
# 31. Grade calculation based on marks.
# 32. Check if a number is a multiple of 7.
# 33. Check if a number is a palindrome.
# 34. Check if a character is an alphabet.
# 35. Check if a number is a three-digit number.
# 36. Calculate electricity bill.
# 37. Calculate income tax based on slabs.
# 38. Find roots of a quadratic equation.
# 39. Check triangle validity.
# 40. Find type of triangle.