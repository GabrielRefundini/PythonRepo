# Write a function called make_album() that builds a dictionary describing a music album. 
# The function should take in an artist name and an album title, and it should return a dictionary containing these two
# pieces of information. 
# Use the function to make three dictionaries representing different albums. 
# Print each return value to show that the dictionaries are storing the album information correctly.

# Use None to add an optional parameter to make_album() that allows you to store the number of songs on an album.
# If the calling line includes a value for the number of songs, add that value to the album’s dictionary. 
# Make at least one new function call that includes the number of songs on an album.

def make_album(artist, album, songs=None):
    full_album = {
        "artist" : artist,
        "album" : album}
    if songs:
        full_album['songs'] = songs
    return full_album
album1 = make_album("Adele", "SkyFall")
album2 = make_album("Taylor Swift", "1989", 13)
album3 = make_album("Ed Sheeran", "Divide", 12)

# Print the album dictionaries
print(album1)
print(album2)
print(album3)