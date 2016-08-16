# 8-8 User Albums

def make_album(artist, album, tracknum=''):
	'''Creates a dictionary of music albums'''
	if tracknum:
		aldict = {
			'album_artist': artist, 'album_name': album, 
			'num_of_tracks': tracknum
			}
	else:
		aldict = {
			'album_artist': artist, 'album_name': album
			}
	return aldict

# allow for user input
album_dict = {}
while True:
	print("Let's compile your favorite artists and albums!")
	print("Note: You can type 'quit' at any time to stop the program.")

	ar = input("What's the name of the artist? ")
	if ar == 'quit':
		break
	al = input("What's the name of the album? ")
	if al == 'quit':
		break
	tr = input("Optional: How many tracks are on the album?" +
		"\n(Note: Just press 'Enter' if you don't know) ")
	if tr == 'quit':
		break

	album_dict = make_album(ar.title(), al.title(), tr)
	print(album_dict)