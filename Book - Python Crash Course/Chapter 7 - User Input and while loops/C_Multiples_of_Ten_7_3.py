# Ask the user for a number, and then report whether the number is a multiple of 10 or not.
number = input("Please insert a number: ")
number = int(number)
if number % 10 == 0:
    print("Yeah, this number is a multiple of 10")
else:
    print("Its not a multiple of 10")