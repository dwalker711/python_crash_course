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

	def guest_count(self):
		'''Print count of guests that have been served.'''
		print(str(self.number_served) + " guests have currently been served.")

	def set_number_served(self, num_guests):
		'''Sets the number of guests served.'''
		self.number_served = num_guests

	def increment_number_served(self, num_gests2):
		'''Add the amount to the count of guests.'''
		self.number_served += num_gests2

r1 = Restaurant('carabas', 'italian')
r1.describe_restaurant()

# Manually changing the number of customers served
r1.number_served = 45
r1.guest_count()

# Using a method to set the number of guests that have been served
r1.set_number_served(50)
r1.guest_count()

# Using a method to INCREMENT the number of guests that have been served
r1.increment_number_served(-12)
r1.guest_count()

