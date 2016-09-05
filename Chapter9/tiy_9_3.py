# 9-3 Users

class User():
	'''Creates a user and their attributes.'''

	def __init__(self, first_name, last_name):
		'''Initialize attributes'''
		self.first_name = first_name
		self.last_name = last_name

	def describe_user(self):
		'''Prints User Information'''
		print("\nFirst Name: " + self.first_name.title())
		print("Last Name: " + self.last_name.title())

	def greet_user(self):
		'''Prints a greeting to the user.'''
		print("\nHello, " + self.first_name.title() + "!")
		print("How are you doing today?")

mo = User('ramona', 'walker')
mo.describe_user()
mo.greet_user()

