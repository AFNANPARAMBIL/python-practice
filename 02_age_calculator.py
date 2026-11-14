"""Age Calculator."""

print("Welcome to the Age Calculator!")
year_of_birth = int(input("Please enter your birth year (YYYY): "))
current_year = int(input("Please enter the current year (YYYY): "))
age = current_year - year_of_birth
print("---------------------------------")
print("Your age is:", age)
