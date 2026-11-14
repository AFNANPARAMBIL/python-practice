"""Bill Calculator."""

item = input("Item name: ")
price = float(input("Enter the item price: "))
quantity = float(input("Enter the quantity (kg): "))
total = price * quantity
print("Item:", item)
print("Total:", total)
