print("SavitriBai Phule Pune University")

semester1 = float(input("Enter your Semester 1 SGPA: "))
semester2 = float(input("Enter your Semester 2 SGPA: "))
total_credit_points = int(input("Enter the total number of credits: "))
total_credits = int(input("Enter the total number of credits: "))

choices = {
    1: "CGPA",
    2: "Percentage"
}

print("\nChoose an option:")
for key, value in choices.items():
    print(f"{key}. {value}")

option = int(input("Enter your choice (1 or 2): "))
if option == 1:
    cgpa = total_credit_points / total_credits
    print(f"\nYour CGPA is: {cgpa:.2f}")
elif option == 2:
    percentage = (semester1 * 10) - semester2
    print(f"\nYour Percentage is: {percentage:.2f}%")
else:
    print("\nInvalid choice. Please select either 1 or 2.")

print("\nThank you for using the CGPA and Percentage Calculator!")
    