# 6-11 Cities

# import locale library for formatting
import locale
locale.setlocale(locale.LC_ALL, "")

cities = {
	'Richmond': {
		'location': 'Virginia',
		'population': 220289,
		'yearestab': 1742
		},
	'Atlanta': {
		'location': 'Georgia',
		'population': 463878,
		'yearestab': 1837,
		},
	'Seattle': {
		'location': 'Washington',
		'population': 684451,
		'yearestab': 1852,
		},
	}

# print city name
for city, info in cities.items():
	print("\nCity: " + city)
	print("\tLocation: " + info['location'])
	# use locale library to format population with commas
	print("\tPopulation: " + str(locale.format("%d", info['population'], 
		grouping=True)))
	# alternative to above line, but only where commas are separators (US)
	# print("\tPopulation: " + "{:,}".format(info['population']))
	print("\tYear Established: " + str(info['yearestab']))
