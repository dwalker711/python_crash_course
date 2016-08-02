favorite_languages = {
	'jen': 'python',
	'sarah': 'c',
	'edward': 'ruby',
	'phil': 'python',
	}

for name, language in favorite_languages.items():
	print(name.title() + "'s favorite language is " +
		language.title() + ".")

# Looping through KEYS is the DEFAULT behavior when looping through a dict!
# this:
for name in favorite_languages.keys():
	print(name.title())

# is the same as this:
for name in favorite_languages:
	print(name.title())
