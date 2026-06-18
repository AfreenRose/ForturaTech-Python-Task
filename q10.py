pizza = 200
burger = 100

pizza_qty = int(input("Pizza Quantity: "))
burger_qty = int(input("Burger Quantity: "))

total = (pizza * pizza_qty) + (burger * burger_qty)

gst = total * 5 / 100

grand_total = total + gst

print("Total Amount:", grand_total)

