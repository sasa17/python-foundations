item = input("Item (enter \"done\" when finished):")

receipt_list = []

while item != 'done':
	price = float(input("Price:"))
	quantity = int(input("Quantity:")) 

	receipt = {}
	receipt['name'] = item
	receipt['quantity'] = quantity
	receipt['price'] = price

	receipt_list.append(receipt)
	item = input("Item (enter \"done\" when finished):")

print('---------------')
print("receipt")
print('---------------')

total = 0

for items in receipt_list: 
	print( "%d %s %.3f KWD" % (items['quantity'], items['name'], (items['price'] * items['quantity'])))
	total += (items['price'] * items['quantity'])

print('---------------')

print('Total Price: %.3f KWD' % total)

