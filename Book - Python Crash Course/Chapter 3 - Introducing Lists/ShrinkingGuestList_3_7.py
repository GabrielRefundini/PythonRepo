# You just found out that your new dinner table won’t arrive in time for the dinner, and now you have space for only two guests.

# Start with your program from Exercise 3-6. Add a new line that prints a message saying that you can invite only two people for dinner.
# Use pop() to remove guests from your list one at a time until only two names remain in your list. Each time you pop a name from your list, 
# print a message to that person letting them know you’re sorry you can’t invite them to dinner.

# Print a message to each of the two people still on your list, letting them know they’re still invited.
# Use del to remove the last two names from your list, so you have an empty list. Print your list to make sure you actually
# have an empty list at the end of your program.

from MoreGuests_3_6 import guest_list
print(guest_list)
message01 = guest_list.pop(0)
message02 = guest_list.pop(0)
message03 = guest_list.pop(1)
message04 = guest_list.pop(1)
print(f"\nI regret to inform you Mr. {message01} that due to unforeseen circumstances, the dinner event has been canceled. Unfortunately, I can only invite two guests, and the table will not arrive in time for the gathering. I hope to have the honor of hosting you at a future event.")
print(f"\nI regret to inform you Mr. {message02} that due to unforeseen circumstances, the dinner event has been canceled. Unfortunately, I can only invite two guests, and the table will not arrive in time for the gathering. I hope to have the honor of hosting you at a future event.")
print(f"\nI regret to inform you Mr. {message03} that due to unforeseen circumstances, the dinner event has been canceled. Unfortunately, I can only invite two guests, and the table will not arrive in time for the gathering. I hope to have the honor of hosting you at a future event.")
print(f"\nI regret to inform you Ms. {message04} that due to unforeseen circumstances, the dinner event has been canceled. Unfortunately, I can only invite two guests, and the table will not arrive in time for the gathering. I hope to have the honor of hosting you at a future event.")

print("\n+--------------------+")
print(f"\nI am pleased to inform you Mr. {guest_list[0]} that you are still invited to join us.")
print(f"\nI am pleased to inform you Ms. {guest_list[1]} that you are still invited to join us.")
print("\n+--------------------+")
del guest_list[0:2] #remove indice 0 AND 1
print(guest_list)
print("\n+--------------------+")
