# 8-6 City Names

def city_country(city, country):
	'''Takes in the name of a city and county'''
	cc = city + ", " + country
	return cc.title()

# user can define how many times they want to enter a city/country
times = input("How many cities would you like to enter?" + 
	"\nPlease enter a number greater than 0: ")

for i in range(0, int(times)):
	city1 = input("Please provide a city: ")
	country1 = input("Now provide a country: ")

	formatted_cc = city_country(city1,country1)
	print("Here's your input: " + formatted_cc)
