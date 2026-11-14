"""Mobile Recharge Calculator."""

amount = float(input("Enter recharge amount: "))
gst = float(input("Enter GST in percentage: "))
gst_amount = amount * gst / 100
print("GST AMOUNT:", gst_amount)
print("Final Amount:", amount + gst_amount)
