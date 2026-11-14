"""Shopping Receipt."""

product1 = input("Enter the name of product 1: ")
price1 = float(input("Enter the price of product 1: "))
product2 = input("Enter the name of product 2: ")
price2 = float(input("Enter the price of product 2: "))
product3 = input("Enter the name of product 3: ")
price3 = float(input("Enter the price of product 3: "))
total = price1 + price2 + price3
print("--- Shopping Receipt ---")
print(product1, ":", price1)
print(product2, ":", price2)
print(product3, ":", price3)
print("The total purchase amount is:", total)
