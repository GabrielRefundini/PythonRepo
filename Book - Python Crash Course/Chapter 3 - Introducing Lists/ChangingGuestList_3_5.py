# You just heard that one of your guests can’t make the dinner, so you need to send out a new set of invitations.
# You’ll have to think of someone else to invite.

# Start with your program from Exercise 3-4. Add a print() call at the end of your program, stating the name of the guest who can’t make it.
# Modify your list, replacing the name of the guest who can’t make it with the name of the new person you are inviting.
# Print a second set of invitation messages, one for each person who is still in your list.
from GuestList_3_4 import guest_list
print(f"{guest_list[1]} appreciates the kind invitation but unfortunately must decline, as he is unable to attend.")
guest_list.remove('Winston Churchill')
guest_list.insert(2, "Marie Curie")
print(f"Dear Mrs. {guest_list[2]}, it would be a great honor to have you as my guest for dinner, where we could discuss your groundbreaking work in science and its impact on the world.")
