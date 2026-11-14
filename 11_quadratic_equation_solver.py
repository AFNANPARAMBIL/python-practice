"""Solve quadratic equations, including complex roots."""

import math
import cmath

a = float(input("Enter coefficient a: "))
b = float(input("Enter coefficient b: "))
c = float(input("Enter coefficient c: "))

if a == 0:
    print("Not a quadratic equation (a cannot be zero).")
else:
    discriminant = b * b - 4 * a * c
    if discriminant > 0:
        root1 = (-b + math.sqrt(discriminant)) / (2 * a)
        root2 = (-b - math.sqrt(discriminant)) / (2 * a)
        print("Roots are real and different.")
        print("Root 1 =", root1)
        print("Root 2 =", root2)
    elif discriminant == 0:
        root = -b / (2 * a)
        print("Roots are real and equal.")
        print("Root 1 = Root 2 =", root)
    else:
        root1 = (-b + cmath.sqrt(discriminant)) / (2 * a)
        root2 = (-b - cmath.sqrt(discriminant)) / (2 * a)
        print("Roots are complex and different.")
        print("Root 1 =", root1)
        print("Root 2 =", root2)
