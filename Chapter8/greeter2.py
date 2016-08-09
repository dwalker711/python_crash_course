def get_formatted_name(firstname, lastname):
	'''Return a full name, neatly formatted.'''
	fullname = firstname + ' ' + lastname
	return fullname.title()

# This is an infinite loop!
while True:
	print("\nPlease tell me your name:")
	f_name = input("First name: ")
	l_name = input("Last name: ")

	formatted_name = get_formatted_name(f_name, l_name)
	print("\nHello, " + formatted_name + "!")
