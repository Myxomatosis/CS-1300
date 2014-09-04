# Lab 2 Calculations
# Author: Luciano Mejia
# Date: 9/4/14
# This program calculates the final price of a purchase after sales tax

sales_tax = .0735
num_items = int(input("Number of Items: "))
cost_per_item = float(input("Cost per item: "))

# num_items = int(num_items_str)
# cost_per_item = float(cost_per_item_str)

price_before_tax = cost_per_item * num_items	# Cost before sales tax is added
price = (price_before_tax * sales_tax) + price_before_tax # Final price, sales tax included

print ("The price is $%.2f" % price)