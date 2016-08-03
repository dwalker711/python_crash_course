# looping through the VALUES in the dictionary
favorite_languages = {
	'jen': 'python',
	'sarah': 'c',
	'edward': 'ruby',
	'phil': 'python',
	}

print("The following languages have been mentioned (not unique):")
for language in favorite_languages.values():
	print(language.title())

'''This does the same thing as the above block, but set() only shows the
unique values'''
print("The following unique languages have been mentioned:")
for language in set(favorite_languages.values()):
	print(language.title())