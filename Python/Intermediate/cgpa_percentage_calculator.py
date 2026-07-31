print("Savitribai Phule Pune University")

semester1 = float(input("Enter Semester 1 SGPA: "))
semester2 = float(input("Enter Semester 2 SGPA: "))

credits1 = int(input("Enter Semester 1 Credits: "))
credits2 = int(input("Enter Semester 2 Credits: "))

choices = {
    1: "CGPA",
    2: "Percentage"
}

print("\nChoose an option:")
for key, value in choices.items():
    print(f"{key}. {value}")

option = int(input("\nEnter your choice (1 or 2): "))

# Weighted CGPA
cgpa = ((semester1 * credits1) + (semester2 * credits2)) / (credits1 + credits2)

if option == 1:
    print(f"\nYour CGPA is: {cgpa:.2f}")

elif option == 2:
    # Simple conversion (CGPA out of 10 → Percentage)
    percentage = cgpa * 10
    print(f"\nYour Percentage is: {percentage:.2f}%")

else:
    print("\nInvalid choice!")

print("\nThank you for using the CGPA & Percentage Calculator!")