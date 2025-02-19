# A number raised to the third power is called a cube. For example, the cube of 2 is written as 2**3 in Python. 
# Make a list of the first 10 cubes (that is, the cube of each integer from 1 through 10), and use a for loop to print out the value of each cube.
cube = [1,2,3,4,5,6,7,8,9,10]

for number in cube:
    number = number**3
    print(number)