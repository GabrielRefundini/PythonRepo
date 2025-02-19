# Cube Comprehension: Use a list comprehension to generate a list of the first 10 cubes.

cube = [number for number in range(1,11,1)]
for number in cube:
    number = number**3
    print(number)