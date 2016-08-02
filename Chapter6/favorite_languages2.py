favorite_languages = {
	'jen': 'python',
	'sarah': 'c',
	'edward': 'ruby',
	'phil': 'python',
	}

friends = ['phil', 'sarah']
for name in favorite_languages.keys():
	print(name.title())

	if name in friends:
		print(" Hi " + name.title() +
			", I see your favorite language is " +
			favorite_languages[name].title() + "!")

# check to see if Erin is on the list
if 'erin' not in favorite_languages.keys():
	print("\nErin, please take our poll!")

# looping through the dictionary's keys in ORDER
# sort the keys as they're returned in the for loop
for name in sorted(favorite_languages.keys()):
	print(name.title() + ", thank you for taking the poll.")