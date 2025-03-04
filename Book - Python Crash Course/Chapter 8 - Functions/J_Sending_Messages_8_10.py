# Start with a copy of your program from Exercise 8-9.
# Write a function called send_messages() that prints each text message and moves each message to a new list 
# called sent_messages as it’s printed. After calling the function, print both of your lists to make sure
# the messages were moved correctly.

def show_messages(messages):
    """Print all messages in the list."""
    for message in messages:
        print(message)

def send_messages(messages, sent_messages):
    """Print all messages in the list and move each message to a new list."""
    while messages:
        current_message = messages.pop()
        print(current_message)
        sent_messages.append(current_message)


sent_messages =[]

text_messages = [
    "Hey, how's it going?",
    "Let's catch up soon!",
    "Don't forget to bring your keys.",
    "Can you pick up some groceries?",
    "Just wanted to check in.",
    "Thanks for the help today!",
    "Have a great day!",
    "Happy birthday! Hope you have an amazing day!",
    "Are you free later this afternoon?",
    "Looking forward to the weekend!"
]

# show_messages(text_messages)
send_messages(text_messages, sent_messages)