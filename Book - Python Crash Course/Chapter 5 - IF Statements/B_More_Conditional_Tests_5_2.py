# You don’t have to limit the number of tests you create to 10. If you want 
# to try more comparisons, write more tests and add them to 
# conditional_tests.py.

# Have at least one True and one False result for each of the following:
# Tests for equality and inequality with strings
# Tests using the lower() method
# Numerical tests involving equality and inequality, greater than and less than,
# greater than or equal to, 
# and less than or equal to Tests using the and keyword and the or keyword
# Test whether an item is in a list
# Test whether an item is not in a list
user = 'Admin'
print("is user == 'admin' true? I predict yes using the lower() method")
print (user.lower() == 'admin')

summcheck = 50
summcheck2 = 40
print("is the summ of summchecks superior to 70? Yes, true.")
print(summcheck + summcheck2 > 70)

print("are the summcheck and summcheck2 superior or equal to 45? No, false.")
print(summcheck and summcheck2 >= 45 )

numbers = [numbers for numbers in range(1,11,1)]
print("is the number 5 in the list? Yes, i predict its true")
print(5 in numbers)

print("is the number 15 in the list? No, i predict its false")
print(15 in numbers)

print("is the number 99 isn't in the list? Correct, i predict its true")
print(99 not in numbers)

#...