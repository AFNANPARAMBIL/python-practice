"""Simple Interest Calculator."""

principal = float(input("Enter Principal Value: "))
rate = float(input("Enter Annual Interest Rate: "))
time = float(input("Enter Time Period (years): "))
simple_interest = principal * rate * time / 100
print("Simple Interest:", simple_interest)
