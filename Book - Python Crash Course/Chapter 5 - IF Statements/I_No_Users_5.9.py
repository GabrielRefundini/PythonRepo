# Add an if test to hello_admin.py to make sure the list of users is not empty.

# If the list is empty, print the message We need to find some users!
# Remove all of the usernames from your list, and make sure the correct message is printed.

usernames = ["admin", "johndoe", "alice123", "bob_the_builder", "charlie_rocks", "user42"]
if usernames:
    for username in usernames:
        if username == 'admin':
            print("Hello admin, would you like to see a status report?")
        else:
            print(f"welcome {username}")
else:
    print("We need to find some users!")