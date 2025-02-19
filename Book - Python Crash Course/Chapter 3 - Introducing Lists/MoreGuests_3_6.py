#You just found a bigger dinner table, so now more space is available. Think of three more guests to invite to dinner.

# Start with your program from Exercise 3-4 or 3-5. Add a print() call to the end of your program, informing people that you found a bigger table.
# Use insert() to add one new guest to the beginning of your list.
# Use insert() to add one new guest to the middle of your list.
# Use append() to add one new guest to the end of your list.
# Print a new set of invitation messages, one for each person in your list.
from ChangingGuestList_3_5 import guest_list
guest_list.insert(0, "Albert Einstein")
guest_list.insert(2, "Leonardo da Vinci")
guest_list.append("Ada Lovelace")
print("I am pleased to inform you that I have secured a larger table for the guests, and I have selected three additional distinguished individuals to join us: Albert Einstein, Leonardo da Vinci, and Ada Lovelace.")
print(f"Dear Mr. {guest_list[0]}, it would be a true honor to have you join us for dinner, where your groundbreaking contributions to physics and your insights into the universe would be deeply appreciated.")
print(f"Dear Mr. {guest_list[1]}, it would be an honor to host you for dinner at my home, where we could discuss important matters of leadership and history.")
print(f"Dear Mr. {guest_list[2]}, I would be delighted to have you as my guest for dinner, where your genius in both the arts and sciences will undoubtedly inspire rich and thought-provoking conversation.")
print(f"Dear Mr. {guest_list[3]}, it would be a pleasure to have you for dinner at my home, where we could exchange ideas on innovation and the future of technology.")
print(f"Dear Ms. {guest_list[4]}, it would be an immense privilege to have you as my guest for dinner, to discuss your visionary work in computing and the profound impact it continues to have on modern technology.")
