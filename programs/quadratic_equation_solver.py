"""Solve ax² + bx + c = 0, including complex roots."""
import cmath
import math


def solve_quadratic(a, b, c):
    if a == 0:
        raise ValueError("a cannot be zero for a quadratic equation")
    discriminant = b * b - 4 * a * c
    if discriminant > 0:
        delta = math.sqrt(discriminant)
        return "Two distinct real roots", ((-b + delta) / (2 * a), (-b - delta) / (2 * a))
    if discriminant == 0:
        root = -b / (2 * a)
        return "One repeated real root", (root, root)
    delta = cmath.sqrt(discriminant)
    return "Two complex roots", ((-b + delta) / (2 * a), (-b - delta) / (2 * a))


def main():
    try:
        a = float(input("Enter coefficient a: "))
        b = float(input("Enter coefficient b: "))
        c = float(input("Enter coefficient c: "))
        kind, roots = solve_quadratic(a, b, c)
    except ValueError as error:
        print(f"Error: {error}")
        return
    print(kind)
    print(f"Root 1: {roots[0]}")
    print(f"Root 2: {roots[1]}")

if __name__ == "__main__":
    main()
