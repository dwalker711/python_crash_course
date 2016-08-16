# 8-12 Sandwiches
def sandwich(*toppings):
	print("\nI'll put the following toppings on your sammich:")
	for t in toppings:
		print("- " + t)

sandwich('cheese')
sandwich('bacon', 'lettuce', 'tomato')