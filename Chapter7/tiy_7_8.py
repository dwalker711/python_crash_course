# 7-8 Deli
sandwich_orders = ['philly', 'BLT', 'reuben', 'fried fish', 'turkey and mayo']

finished_sandwiches = []

while sandwich_orders:
	current_sandwich = sandwich_orders.pop()
	print("I have finished making your " + current_sandwich + " sandwich!")

	finished_sandwiches.append(current_sandwich)

# Display finished sandwiches
print("\nThe following sandwiches have been completed:")
for sandwich in finished_sandwiches:
	print(sandwich)