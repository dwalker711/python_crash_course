# 8-14 Cars
def car_profile(make, model, **other):
	'''Stores information about a car in a dictionary'''
	profile = {}
	profile['manufacturer'] = make.title()
	profile['car_model'] = model
	for k,v in other.items():
		profile[k] = v
	return profile

mycar = car_profile('Mazda', '3', color='white', type='sedan')
print(mycar)
