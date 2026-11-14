"""Electricity Bill Estimator.

Accept units consumed and cost per unit. Calculate the estimated bill.
"""

units = float(input("Enter units consumed: "))
cost_per_unit = float(input("Enter cost per unit: "))
estimated_bill = units * cost_per_unit
print("The electricity bill is:", estimated_bill)
