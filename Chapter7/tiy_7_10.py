# 7-10 Dream Vacation

print("\nHello! This is a poll about dream vacations.")

responses = {}

active = True

while active:
	name = input("What is your name? ")
	resp = input("If you could visit one place in the world for vacation," + 
		" where would it be? ")
	responses[name] = resp
	cont = input("Would you like to let another person respond? (yes/no)")

	if cont == 'no':
		active = False

print("\n--- Here are the results of the Dream Vacay Poll: ---")
for name, resp in responses.items():
	print(name + " would like to travel to " + resp + ".")
