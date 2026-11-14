"""BMI Calculator."""

height = float(input("Enter your height in metres: "))
weight = float(input("Enter your weight in kilograms: "))
if height <= 0:
    print("Height must be greater than zero.")
else:
    bmi = weight / height ** 2
    print("Your BMI is:", round(bmi, 2))
