# using a function to retrn a dictionary
def build_person(firstname, lastname, age=''):
	'''Return a dictionary of information about a person.'''
	person = {'first': firstname, 'last': lastname}
	if age:
		person['age'] = age
	return person

musician = build_person('jimi', 'hendrix', age=27)
print(musician)
