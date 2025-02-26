# Use a dictionary to store people’s favorite numbers. 
# Think of five names, and use them as keys in your dictionary. Think of a favorite number for each person,
# and store each as a value in your dictionary. 
# 
# Print each person’s name and their favorite number. 
# For even more fun, poll a few friends and get some actual data for your program.
persons = {
    'Gabriel': 3,
    'Rafael' : 10,
    'Jorge' : 77,
    'Harry' : 91,
    'Cristiano' : 44
}

for name, number in persons.items():
    print(f"{name} has the {number} as a favorite number")