# Using one of the programs you wrote in this chapter, add several lines to the end of the program that do the following:

multiples =[ number for number in range(3,31, 3)]
print(multiples)

# Print the message The first three items in the list are:. Then use a slice to print the first three items from that program’s list.
print(f"The first three items in the list are: {multiples [:3]}")
# Print the message Three items from the middle of the list are:. Then use a slice to print three items from the middle of the list.
print(f" Three items from the middle of the list are: {multiples[4:7]}")
# Print the message The last three items in the list are:. Then use a slice to print the last three items in the list.
print(f"The last three items in the list are: {multiples[-3:]}")
