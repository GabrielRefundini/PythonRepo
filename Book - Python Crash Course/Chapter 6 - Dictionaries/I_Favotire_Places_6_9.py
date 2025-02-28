# Make a dictionary called favorite_places. 
# Think of three names to use as keys in the dictionary, and store one to three favorite places for each person. 

# To make this exercise a bit more interesting, ask some friends to name a few of their favorite places. 
# Loop through the dictionary, 
# and print each person’s name and their favorite places.

favorite_places = {
    'Grazielle' : ['Toscana'],
    'Gabriel' : ['Bed Room', 'Vienna'],
    'Ted' : ['Soccer field']
}
for key, value in favorite_places.items():
    print(f"{key}'s favorite places: value {', '.join(value)}")