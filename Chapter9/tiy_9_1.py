# 9-1 Restaurant

class Restaurant():
	'''Modeling a restaurant.'''

	def __init__(self, restaurant_name, cuisine_type):
		'''Initialize restaurant name and cuisine.'''
		self.restaurant_name = restaurant_name
		self.cuisine_type = cuisine_type

	def describe_restaurant(self):
		'''Prints information about restaurant.'''
		print("\nThe restaurant name is " + self.restaurant_name.title() + ".")
		print("The genre of cuisine is " + self.cuisine_type.title() + ".")

	def open_restaurant(self):
		'''Prints messge indicating the restaurant is open.'''
		print("\n" + self.restaurant_name + " is now open.")

'''
restaurant = Restaurant("Olive Garden", "Italian")
print("I can't wait to go to " + restaurant.restaurant_name.title() + "!")
restaurant.describe_restaurant()
restaurant.open_restaurant()
'''
