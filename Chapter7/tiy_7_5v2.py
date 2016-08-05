# Movie Tickets, Version 2
prompt = "Welcome to MovieMax! Can I please have your age?"
prompt += "\n(Type 'quit' to leave at any time) Your age: "

while True:
	age = input(prompt)

	if age == 'quit':
		print("\nHave a nice day!")
		break

	else:
		try:
			if int(age) < 3:
				print("Your admission is free!")
			elif 3 <= int(age) <= 12:
				print("Your ticket price will be $10 dollars.")
			elif int(age) > 12:
				print("Your ticket price is $15 dollars.")
		except ValueError:
			print("(I'm sorry, what was that?\nPlease enter a valid number," +
				" or type 'quit' to exit.)")
			continue

