"""Practice checking age-based voting eligibility (18-year threshold)."""
age = int(input("Enter your age: "))
if age < 0:
    print("Age cannot be negative.")
elif age >= 18:
    print("You meet the age threshold to vote.")
else:
    print("You are below the voting age threshold.")
