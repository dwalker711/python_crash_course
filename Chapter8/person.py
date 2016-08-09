# using a function to retrn a dictionary
def build_person(firstname, lastname):
	'''Return a dictionary of information about a person.'''
	person = {'first': firstname, 'last': lastname}
	return person

musician = build_person('jimi', 'hendrix')
print(musician)
