# 8-3 Cities
def make_shirt(size, message):
	"""Shows the size of the t-shirt and printed message"""
	print("This shirt is a size " + size.title() + ", and prints the message: " + 
		message.title())

make_shirt('large', 'Hello!')
make_shirt(message='just do it.', size='extra large')

