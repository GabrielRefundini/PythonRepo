# Start with the program you wrote for Exercise 6-1 (page 98). 
# Make two new dictionaries representing different people, and store all three dictionaries in a list called people. 
# Loop through your list of people. As you loop through the list, print everything you know about each person.

people = []
person1 = {
    'name' : 'Zelda',
    'last_name' : 'Ocarian',
    'age' : '25',
    'city' : 'Hyrule'
}

person2 = {
    'name' : 'John',
    'last_name' : 'Spark',
    'age' : '30',
    'city' : 'Tokyo'
}

person3 = {
    'name' : 'Carol',
    'last_name' : 'Yang',
    'age' : '22',
    'city' : 'Beijing'
}

people.extend([person1, person2, person3])

for person in people:
    print(f"First Name: {person['name']}")
    print(f"Last Name: {person['last_name']}")
    print(f"Age: {person['age']}")
    print(f"City: {person['city']}\n")