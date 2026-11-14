"""Shopping bill with discount, GST and delivery (classroom exercise)."""

item = input("Item: ")
price = float(input("Price: "))
qty = int(input("Quantity: "))
member = input("Member (y/n): ").strip().lower()

if price <= 0 or qty <= 0:
    print("Error: Price and quantity must be greater than 0.")
else:
    subtotal = price * qty
    if subtotal >= 5000:
        discount_rate = 10
    elif subtotal >= 2000:
        discount_rate = 5
    else:
        discount_rate = 0
    if member == "y":
        discount_rate += 2

    discount = subtotal * discount_rate / 100
    after_discount = subtotal - discount
    gst = after_discount * 18 / 100
    before_delivery = after_discount + gst
    delivery = 0 if before_delivery > 1000 else 50
    total = before_delivery + delivery

    print("\n________ BILL ________")
    print("Item        :", item)
    print("Subtotal    :", f"{subtotal:.2f}")
    print("Discount    :", f"{discount:.2f} ({discount_rate}%)")
    print("GST (18%)   :", f"{gst:.2f}")
    print("Delivery    :", "Free" if delivery == 0 else f"{delivery:.2f}")
    print("TOTAL       :", f"{total:.2f}")
