"""Calculate the area of a triangle."""
base = float(input("Enter triangle base: "))
height = float(input("Enter triangle height: "))
if base <= 0 or height <= 0:
    print("Base and height must be positive.")
else:
    print("Triangle area:", 0.5 * base * height)
