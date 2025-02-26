# Modify your program from Exercise 6-2 (page 98) so each person can have more than one favorite number. 
# Then print each person’s name along with their favorite numbers.
persons = {
    'Gabriel': [3,33,333],
    'Rafael' : [10,91,11],
    'Jorge' : [77,2],
    'Harry' : [91],
    'Cristiano' : [44, 46, 98]
}

for name, number in persons.items():
    print(f"{name} has the {','.join(map(str,number))} as a favorite number")