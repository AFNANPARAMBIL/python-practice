"""Practice f-strings, formatting, binary numbers and arithmetic."""
pi_approx = 3.14285714
print(f"Pi approximation: {pi_approx:.2f}")
name = "Afnan"
age = 19
print(f"My name is {name} and I am {age} years old.")
for i in range(1, 6):
    print(f"Binary of {i}: {bin(i)}")
a, b = 24, 7
print("Sum:", a + b)
print("Product:", a * b)
print("Difference:", a - b)
print("Division:", a / b)
print("Remainder:", a % b)
print("Floor division:", a // b)
print("Exponent:", a ** b)
