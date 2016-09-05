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


OGarden = Restaurant("Olive Garden", "Italian")
print("I can't wait to go to " + OGarden .restaurant_name.title() + "!")
OGarden.describe_restaurant()
OGarden.open_restaurant()

RLobster = Restaurant("Red Lobster", "Seafood")
print("I don't like " + RLobster.restaurant_name.title() + ".")
RLobster.describe_restaurant()
RLobster.open_restaurant()