# Make several dictionaries, where each dictionary represents a different pet. 
# In each dictionary, include the kind of animal and the owner’s name. Store these dictionaries in a list called pets. 
# Next, loop through your list and as you do, print everything you know about each pet.
dog = {
    'type' : 'dog',
    "owner" : 'Jorge',
    "kind" : 'Mammal'
}

cat = {
    'type' : 'cat',
    "owner" : 'Thaila',
    "kind" : 'Mammal'
}

tiger = {
    'type' : 'tiger',
    "owner" : 'Richard',
    "kind" : 'Mammal'
}

pets = [dog, cat, tiger]

for pet in pets:
    print("Pet Details:")
    for key, value in pet.items():
        print(f"{key}: {value}")