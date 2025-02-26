# Start with your program from Exercise 8-7. Write a while loop that allows users to enter an album’s artist and title. 
# Once you have that information, call make_album() with the user’s input and print the dictionary that’s created. 
# Be sure to include a quit value in the while loop.

def make_album(artist, album, songs=None):
    """Build a dictionary containing information about an album."""
    full_album = {
        "artist" : artist.title(),
        "album" : album.title()
        }
    if songs:
        full_album['songs'] = songs
    return full_album
# Let the user know how to quit.
print("Enter 'q' at any time to quit.")

while True:
    inp_artist = input("Enter the Artist: ")
    if inp_artist == 'q':
        break
    inp_album = input("Enter the album Title: ")
    if inp_album == 'q':
        break
    inp_songs = input("How many songs are in the album: ")
    if inp_songs == 'q':
        break
    album = make_album(inp_artist,inp_album, inp_songs)
    print(album)
