# NOTE: the middle name is last, and is an empty string by default!
def get_formatted_name(firstname, lastname, middlename=''):
	"""Return a full name, neatly formatted"""
	if middlename: # Python interprets non-empty strings as TRUE
		fullname = firstname + ' ' + middlename + ' ' + lastname
	else:
		fullname = firstname + ' ' + lastname
	return fullname.title()

musician = get_formatted_name('jimi', 'hendrix')
print(musician)

musician = get_formatted_name('john', 'hooker', 'lee')
print(musician)
