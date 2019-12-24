a = input("Enter first number:")
b = input("Enter second number:")
sign = input("Choose operation (+, -, /, *):")

if a.isnumeric() and b.isnumeric():
	a = int(a)
	b = int(b)
	if sign == "+":
		result = int(a) + int(b)
		print("The answer is", result)
	elif sign == "-":
		result = int(a) - int(b)
		print("The answer is", result)
	elif sign == "/":
		result = int(a) / int(b)
		print("The answer is", result)
	elif sign == "*":
		result = int(a) * int(b)
		print("The answer is", result)
	else:
		print("Invalid operation")
else:
	print("Invalid number")

