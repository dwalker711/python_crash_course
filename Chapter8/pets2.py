# Keyword arguments are a name-pair value you can pass to a functon
# Order is not a problem with this method
def describe_pet(animal_type, pet_name):
	"""Display information about a pet."""
	print("\nI have a " + animal_type + ".")
	print("My " + animal_type + "'s name is " + pet_name.title() + ".")

describe_pet(animal_type='hamster', pet_name='harry')
describe_pet(pet_name='willie', animal_type='dog')
# Make sure you use the exact parameter names for the functions!!!