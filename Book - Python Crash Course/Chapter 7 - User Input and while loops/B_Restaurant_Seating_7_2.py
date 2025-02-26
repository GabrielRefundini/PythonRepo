# Write a program that asks the user how many people are in their dinner group. If the answer is more than eight,
# print a message saying they’ll have to wait for a table. Otherwise, report that their table is ready.

answer = input("How many people are in your dinne group? ")
answer = int(answer)
if answer > 8:
    print("Sorry, but you'll have to wait a little bit")
else:
    print("Sure, follow me, please.")