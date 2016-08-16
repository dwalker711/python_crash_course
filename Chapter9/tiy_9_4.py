# 9-4 Number Served
class Restaurant():
	'''Modeling a restaurant.'''

	def __init__(self, restaurant_name, cuisine_type):
		'''Initialize restaurant name and cuisine.'''
		self.restaurant_name = restaurant_name
		self.cuisine_type = cuisine_type
		self.number_served = 0

	def describe_restaurant(self):
		'''Prints information about restaurant.'''
		print("\nThe restaurant name is " + self.restaurant_name.title() + ".")
		print("The genre of cuisine is " + self.cuisine_type.title() + ".")

	def open_restaurant(self):
		'''Prints messge indicating the restaurant is open.'''
		print("\n" + self.restaurant_name + " is now open.")

