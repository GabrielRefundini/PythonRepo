# Think of at least five places in the world you’d like to visit.

# Store the locations in a list. Make sure the list is not in alphabetical order.

countries = ["Italy", "Canada", "Egypt", "Greece", "Switzerland", "Japan"]
# Print your list in its original order. Don’t worry about printing the list neatly; just print it as a raw Python list.
print(countries)

# Use sorted() to print your list in alphabetical order without modifying the actual list.
print(sorted(countries))

# Show that your list is still in its original order by printing it.
print (countries)

# Use sorted() to print your list in reverse-alphabetical order without changing the order of the original list.
print(sorted(countries, reverse=True))

# Show that your list is still in its original order by printing it again.
print (countries)

# Use reverse() to change the order of your list. Print the list to show that its order has changed.
countries.reverse()
print(countries)

# Use reverse() to change the order of your list again. Print the list to show it’s back to its original order.
countries.reverse()
print(countries)

# Use sort() to change your list so it’s stored in alphabetical order. Print the list to show that its order has been changed.
countries.sort()
print(countries)

# Use sort() to change your list so it’s stored in reverse-alphabetical order. Print the list to show that its order has changed.
countries.sort(reverse=True)
print(countries)