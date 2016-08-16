# 8-11 Unchanged MAgicians
def show_magicians(names):
	'''prints the name of each magician'''
	for n in names:
		print(n.title())

def make_great(names):
	'''adds 'the Great' to each magicians name'''
	while names:
		current_mag = names.pop()
		print(current_mag.title() + " the Great")
		completed_mag.append(current_mag)

magicians = ['blaine', 'houdini', 'angel']
completed_mag = []

show_magicians(magicians)
make_great(magicians[:])

# to show that a copy of the magicians list was used
print(magicians)
print(completed_mag)