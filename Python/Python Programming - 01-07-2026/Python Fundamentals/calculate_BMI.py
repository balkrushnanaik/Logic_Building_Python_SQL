# 53. Write a program to calculate BMI and classify the person's health status.

def bmi(weight, height):
    total = weight / (height ** 2)

    if total < 18.5:
        status = "Underweight"
    elif total < 25:
        status = "Normal weight"
    elif total < 30:
        status = "Overweight"
    else:
        status = "Obese"

    return total, status


bmi_value, health_status = bmi(56, 1.81)

print(f'BMI: {bmi_value:.2f}')
print(f'Health Status: {health_status}')