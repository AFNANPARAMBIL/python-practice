"""Practice positive/negative/zero, even/odd and number comparison."""
number = int(input("Enter an integer: "))
if number > 0:
    print("Positive")
elif number < 0:
    print("Negative")
else:
    print("Zero")
print("Even" if number % 2 == 0 else "Odd")
a = float(input("Enter first number: "))
b = float(input("Enter second number: "))
if a > b:
    print("First number is greater.")
elif b > a:
    print("Second number is greater.")
else:
    print("Both numbers are equal.")
