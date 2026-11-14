"""Calculate net salary from user-entered pay, allowances and deductions."""
name = input("Employee name: ")
basic_pay = float(input("Basic pay: "))
hra = float(input("HRA: "))
travel_allowance = float(input("Travel allowance: "))
deduction = float(input("Deductions: "))
if min(basic_pay, hra, travel_allowance, deduction) < 0:
    print("Amounts cannot be negative.")
else:
    net_salary = basic_pay + hra + travel_allowance - deduction
    print(f"{name}'s net salary: {net_salary:.2f}")
