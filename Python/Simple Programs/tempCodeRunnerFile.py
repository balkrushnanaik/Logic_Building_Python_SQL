
# # print('Thank you!')

# # # 26. Check voting eligibility.
# # age = 19
# # result = "eligible" if age >= 18 else "not eligible"
# # print(f"You are {result} to vote.")

# # 27. Check whether a character is a vowel or consonant.
# chars = input("Enter a character: ").lower()
# if chars in ['a', 'e', 'i', 'o', 'u']:
#     print(f"{chars} is a vowel.")
# else:
#     print(f"{chars} is a consonant.")

# # 28. Check if a number is divisible by 5 and 11.
# number = int(input("Enter a number: "))
# if number % 5 == 0 and number % 11 == 0:
#     print(f"{number} is divisible by both 5 and 11.")
# else:
#     print(f"{number} is not divisible by both 5 and 11.")
# # 29. Check whether a character is uppercase or lowercase.
# char = input("Enter a character: ")
# if char.isupper():
#     print(f"{char} is uppercase.")
# else:
#     print(f"{char} is lowercase.")
# # 30. Find smallest of three numbers.
# num1 = float(input("Enter first number: "))
# num2 = float(input("Enter second number: "))
# num3 = float(input("Enter third number: "))
# if num1 <= num2 and num1 <= num3:
#     smallest = num1
# elif num2 <= num1 and num2 <= num3:
#     smallest = num2
# else:
#     smallest = num3
# print(f"The smallest number is {smallest}.")
# # 31. Grade calculation based on marks.
# marks = float(input("Enter marks (0-100): "))
# match marks:
#     case m if 90 <= m <= 100:
#         grade = 'A'
#     case m if 80 <= m < 90:
#         grade = 'B'
#     case m if 70 <= m < 80:
#         grade = 'C'
#     case m if 60 <= m < 70:
#         grade = 'D'
#     case m if 0 <= m < 60:
#         grade = 'F'
#     case _:
#         grade = 'Invalid marks'
# print(f"Your grade is {grade}.")

# # 32. Check if a number is a multiple of 7.
# number = int(input("Enter a number: "))
# if number % 7 == 0:
#     print(f"{number} is a multiple of 7.")  
# else:
#     print(f"{number} is not a multiple of 7.")
# # 33. Check if a number is a palindrome.